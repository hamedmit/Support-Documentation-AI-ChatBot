from sentence_transformers import SentenceTransformer
import faiss
import json

# 1. Load the embedding model
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# 2. Read processed documents (including text and URL)
try:
    with open("data/processed_data.json", "r", encoding="utf-8") as f:
        docs = json.load(f)  # Format: [{"text": "Processed text", "url": "Corresponding link"}, ...]
except FileNotFoundError:
    print("❌ Error: processed_data1.json not found!")
    exit(1)
except json.JSONDecodeError:
    print("❌ Error: Failed to decode JSON file!")
    exit(1)

# Extract texts for embedding
texts = [doc["text"] for doc in docs if "text" in doc]

if not texts:
    print("❌ Error: No valid text data found in processed_data1.json")
    exit(1)

# 3. Compute embeddings and store in FAISS
try:
    doc_vectors = embedding_model.encode(texts)  # Convert texts to vectors
    dimension = doc_vectors.shape[1]  # Get embedding dimensions
    index = faiss.IndexFlatL2(dimension)  # Create FAISS index
    index.add(doc_vectors)  # Add vectors to FAISS database
except Exception as e:
    print(f"❌ Error: Failed to compute embeddings or build FAISS index - {e}")
    exit(1)

# 4. Save FAISS database
try:
    faiss.write_index(index, "support_index.faiss")
except Exception as e:
    print(f"❌ Error: Failed to save FAISS index - {e}")
    exit(1)

# 5. Save metadata (text and URLs) for retrieval
try:
    with open("data/doc_metadata.json", "w", encoding="utf-8") as f:
        json.dump(docs, f, ensure_ascii=False, indent=4)
except Exception as e:
    print(f"❌ Error: Failed to save document metadata - {e}")
    exit(1)

print("✅ Documents processed and stored successfully!")
