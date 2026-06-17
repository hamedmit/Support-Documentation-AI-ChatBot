# Support Documentation AI Model (A ChatBot)

## Overview

This project aims to develop an AI-powered system to enhance user experience and accessibility to support documentation. By training a model on support website data, we enable users to efficiently retrieve relevant information via a chatbot interface. This approach improves engagement, reduces support overhead, and ensures seamless access to documentation for inactive users and merchants.

## Project Objectives

- **Automated Information Retrieval**: Develop a model that understands and retrieves relevant support documentation efficiently.
- **Scalability & Adaptability**: Ensure the system can handle diverse content formats and grow with future data expansions.
- **Enhanced User Interaction**: Implement a chatbot-based interface for seamless user queries.

## Methodology

### 1. Model Selection

We evaluated multiple models based on performance, scalability, and adaptability to support documentation. The final selection was **FLAN-T5 Large** due to:

- Strong **natural language understanding** capabilities.
- Ability to **generate concise and relevant answers**.
- Optimized performance for **question-answering tasks**.

Additionally, **SentenceTransformers (all-MiniLM-L6-v2)** was chosen for **semantic search and document embedding**, enabling efficient retrieval of relevant information.

### 2. Data Collection & Preprocessing

A **custom web scraper** was developed to extract structured content from the Support Website, ensuring comprehensive coverage of all relevant pages.

Data preprocessing steps included:

- **Content Normalization**: Standardizing text formats, handling variations in structure and metadata.
- **Embedding Indexing**: Using **FAISS** to store and search document vectors efficiently.

### 3. Querying & Chatbot Integration

The chatbot retrieves responses through a multi-step approach:

1. **Semantic Search**: FAISS retrieves the most relevant documents based on user queries.
2. **Answer Generation**: FLAN-T5 processes retrieved documents and formulates a response.
3. **Interactive UI**: A **Tkinter-based chat interface** allows users to submit queries and receive responses dynamically.

### 4. System Testing & Optimization

Extensive testing was conducted to ensure:

- **Model accuracy** in retrieving and generating correct answers.
- **Scalability** for handling large datasets.
- **User-friendly interaction** with the chatbot interface.

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

1- Run the strong scraper to extract support documentation from the website.

2- Run the normalization processing to standardize and clean the extracted data.

3- Run the FAISS indexing script to create the search index for efficient retrieval.

4- Finally, run the chatbot to interact with the processed support documentation.

Ensure all dependencies are installed before running the scripts.

## Contributors

- **Hamed Qazanfari** - Lead Developer & Researcher

## Future Enhancements

- Fine-tuning the model on custom support queries.
- Improving UI/UX for a better chatbot experience.
- Expanding document coverage with additional sources.

This project provides a robust AI-driven approach to support documentation, improving user accessibility and efficiency in retrieving relevant information.

