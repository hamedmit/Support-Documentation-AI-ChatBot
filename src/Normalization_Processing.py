import json
import re
import unicodedata
import nltk
from nltk.tokenize import sent_tokenize
# Download tokenizer on first run
nltk.download('punkt')


def clean_text(text):
    """Cleans the input text by removing unwanted artifacts and fixing spacing issues."""
    text = re.sub(r'##', '', text)  # Remove '##' artifacts
    text = text.replace('[UNK]', ' ')  # Replace '[UNK]' with space to avoid word merging
    text = unicodedata.normalize("NFKC", text)  # Normalize Unicode characters
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'["\#\%\&\*\+/<>@\[\\\]^_`{|}~]', '', text)  # Remove special symbols
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Remove non-ASCII characters
    text = re.sub(r'\s+', ' ', text).strip()  # Fix extra spaces
    return text


def is_valid_sentence(sentence):
    """Checks if a sentence is meaningful and well-formed."""
    words = sentence.split()
    return len(words) > 3  # Sentences with fewer than 4 words are likely invalid


def process_data(input_file, output_file):
    """Processes the input JSON file, cleans and filters text, and saves the output."""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading input file: {e}")
        return

    processed_data = []

    for item in data:
        paragraphs = [clean_text(p) for p in item.get("paragraphs", []) if p.strip()]
        url = item.get("url", "")  # Keep related URL

        # Remove headers and merge paragraphs
        content = " ".join(paragraphs)

        # Split text into sentences and remove invalid ones
        sentences = sent_tokenize(content)
        valid_sentences = [s for s in sentences if is_valid_sentence(s)]

        # Merge valid sentences into final cleaned text
        final_text = " ".join(valid_sentences)

        # Append to output list while preserving the URL
        if final_text:
            processed_data.append({"text": final_text, "url": url})

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Error writing output file: {e}")
        return

    print("✅ Data normalization and processing completed! Output saved in", output_file)


# Execute the function
process_data("data/extracted_content.json", "data/processed_data.json")
