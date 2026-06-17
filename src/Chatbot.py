import tkinter
import tkinter.scrolledtext as scrolledtext
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import json
import torch
import tensorflow as tf
import webbrowser

# Suppress TensorFlow warnings
tf.get_logger().setLevel('ERROR')

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")


class ModelHandler:
    """Handles model loading and processing for the chatbot."""

    def __init__(self, index_path="support_index.faiss", doc_path="data/doc_metadata.json"):
        self.embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        self.tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large").to(device)
        self.index = faiss.read_index(index_path)

        with open(doc_path, "r", encoding="utf-8") as f:
            self.docs = json.load(f)

    def generate_answer(self, question, context):
        """Generates an answer for a given question based on the context."""
        input_text = f"question: {question} context: {context}"
        input_ids = self.tokenizer(input_text, return_tensors="pt", padding=True, truncation=True).to(device)
        output_ids = self.model.generate(**input_ids, max_length=200)
        return self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

    def find_context(self, question):
        """Finds the most relevant documents for the given question."""
        query_vector = self.embedding_model.encode([question])
        k = 3  # Retrieve top 3 relevant documents
        _, indices = self.index.search(np.array(query_vector), k)

        retrieved_docs = []

        if isinstance(self.docs, dict):
            keys = list(self.docs.keys())
            for i in indices[0]:
                if 0 <= int(i) < len(keys):
                    key = keys[int(i)]
                    retrieved_docs.append((self.docs[key]["text"], self.docs[key]["url"]))

        elif isinstance(self.docs, list):
            for i in indices[0]:
                if 0 <= int(i) < len(self.docs):
                    retrieved_docs.append((self.docs[int(i)]["text"], self.docs[int(i)]["url"]))

        if not retrieved_docs:
            return "No relevant documents found.", None

        context = " ".join([doc[0] for doc in retrieved_docs])
        link = retrieved_docs[0][1]
        return context, link


class ChatInterface:
    """Handles the UI for the chatbot."""

    def __init__(self, master, model_handler):
        self.master = master
        self.model_handler = model_handler
        master.title("Simple Chat")

        self.chat_log = scrolledtext.ScrolledText(master, width=90, height=40, font=("Arial", 12))
        self.chat_log.pack(padx=10, pady=10)
        self.chat_log.config(state=tkinter.DISABLED)

        self.chat_log.tag_config("user", foreground="blue", font=("Arial", 12, "bold"))
        self.chat_log.tag_config("bot", foreground="green", font=("Arial", 12, "bold"))
        self.chat_log.tag_config("link", foreground="purple", font=("Arial", 12, "underline"))

        self.chat_log.tag_bind("link", "<Enter>", lambda e: self.chat_log.config(cursor="hand2"))
        self.chat_log.tag_bind("link", "<Leave>", lambda e: self.chat_log.config(cursor="arrow"))

        self.input_field = tkinter.Entry(master, width=50, font=("Arial", 12))
        self.input_field.pack(padx=10, pady=5)
        self.input_field.bind("<Return>", self.send_message)

        self.send_button = tkinter.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

    def send_message(self, event=None):
        message = self.input_field.get().strip()
        if message:
            if not message.endswith("?"):
                message += "?"
            self.display_message(f"You: {message}", "user")
            self.input_field.delete(0, tkinter.END)
            response = self.get_response(message)
            self.display_message(response, "bot")

    def display_message(self, message, tag):
        """Displays messages in the chat window with appropriate styling."""
        self.chat_log.config(state=tkinter.NORMAL)
        self.chat_log.insert(tkinter.END, message + "\n", tag)
        self.chat_log.config(state=tkinter.DISABLED)
        self.chat_log.see(tkinter.END)

    def display_link(self, link):
        """Displays a clickable link in the chat window."""
        self.chat_log.config(state=tkinter.NORMAL)
        self.chat_log.insert(tkinter.END, "Click here for more details\n", "link")
        self.chat_log.tag_bind("link", "<Button-1>", lambda e: webbrowser.open_new(link))
        self.chat_log.config(state=tkinter.DISABLED)
        self.chat_log.see(tkinter.END)

    def get_response(self, question):
        context, link = self.model_handler.find_context(question)
        answer = self.model_handler.generate_answer(question, context)
        response = f"Bot: {answer}\n"

        if link:
            self.display_link(link)

        return response


if __name__ == '__main__':
    root = tkinter.Tk()
    model_handler = ModelHandler()
    chat_interface = ChatInterface(root, model_handler)
    root.mainloop()
