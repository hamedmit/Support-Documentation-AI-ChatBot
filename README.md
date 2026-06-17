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
```
User Query
↓
Semantic Search (FAISS)
↓
Relevant Documents
↓
FLAN-T5
↓
Generated Answer
```
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

## Roadmap

- [ ] Improve chatbot UI
- [ ] Add web-based frontend
- [ ] Support additional documentation sources
- [ ] Add evaluation metrics
- [ ] Docker support

---

## Contributing

Contributions are welcome.

If you would like to improve the project, please check the open issues or create a new one describing your proposal.

All kinds of contributions are appreciated, including:

- Bug fixes
- Documentation improvements
- Frontend/UI enhancements
- New features
- Performance optimizations


## Author

**Hamed Qazanfari** - Researcher and AI Engineer

## Support

If you find this project useful, consider starring the repository and sharing feedback through issues or discussions.

Contributions, suggestions, and feature requests are always welcome.
  ---

## Example Queries

You can ask the chatbot questions such as:

- "How can I reset my account password?"
- "Where can I find the user documentation?"
- "How do I troubleshoot login issues?"
- "What are the available support resources?"

---

## Troubleshooting

### ModuleNotFoundError

If you encounter missing package errors, make sure all dependencies are installed:

```bash
pip install -r requirements.txt
```

### FAISS or model loading issues

Ensure the required models and indexing files are created by running the setup scripts in the correct order.

### Application does not start

Verify that Python is installed correctly and that you are running the scripts from the project root directory.

```
