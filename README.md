# Support Documentation AI Chatbot

> AI-powered support documentation chatbot using FLAN-T5, FAISS, and semantic search.

This project was originally developed in 2025 as part of an AI engineering project focused on intelligent support-documentation retrieval and question answering.

---

## Features

- Web scraping for support documentation
- Text normalization and preprocessing
- Semantic search using SentenceTransformers
- FAISS-based vector indexing
- FLAN-T5 answer generation
- Interactive chatbot interface
- Extensible architecture for new documentation sources

---

## Architecture

User Query
↓
Semantic Search (FAISS)
↓
Relevant Documents
↓
FLAN-T5
↓
Generated Answer

---

## Tech Stack

- Python
- FLAN-T5 Large
- SentenceTransformers
- FAISS
- Tkinter
- BeautifulSoup
- Requests

---

## Project Structure

```
project_root/
│── data/                               # Processed and raw support documentation
│── models/                             # Pretrained and fine-tuned model files
│── src/                                # Source code
│   │── Strong_scraper.py               # Web scraper for support documentation
│   │── Normalization_Processing.py     # Data normalization
|   |── Faiss_Indexing.py               # Faiss indexing
│   │── chatbot.py                      # Chatbot interface and querying
│── requirements.txt                    # Dependencies
│── README.md                           # Project documentation
```

## Installation & Setup

### Prerequisites

Ensure you have Python 3.8+ installed. Then, install dependencies:

```bash
pip install -r requirements.txt
```

To set up and run the project, follow these steps in order:

1- Run the strong scraper to extract support documentation from the website. (or ``` python src/Strong_scraper.py ```)

2- Run the normalization processing to standardize and clean the extracted data. (or ``` python src/Normalization_Processing.py ```)

3- Run the FAISS indexing script to create the search index for efficient retrieval. (or ``` python src/Faiss_Indexing.py ```)

4- Finally, run the chatbot to interact with the processed support documentation. (or ``` python src/chatbot.py ```)

Ensure all dependencies are installed before running the scripts.

Roadmap
 Improve chatbot UI
 Add web-based frontend
 Support additional documentation sources
 Add evaluation metrics
 Docker support


## Contributors

- **Hamed Qazanfari** - Researcher and AI Engineer

## Future Enhancements

- Fine-tuning the model on custom support queries.
- Improving UI/UX for a better chatbot experience.
- Expanding document coverage with additional sources.

This project provides a robust AI-driven approach to support documentation, improving user accessibility and efficiency in retrieving relevant information.

