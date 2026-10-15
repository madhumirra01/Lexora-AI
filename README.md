# ✨ Lexora AI — Text Summarization

**Less text. More insight.**

Lexora AI is a lightweight text summarization web application that converts lengthy articles, reports, and other text into concise summaries using the **TextRank algorithm**. Built with Python and Streamlit, it provides a simple interface for extracting important information from text.

## 🚀 Features

- **Text summarization:** Extracts important sentences from the input text using TextRank.
- **Adjustable summary length:** Choose the number of sentences in the generated summary.
- **Summary statistics:** View original word count, summary word count, and text reduction percentage.
- **Download summaries:** Save generated summaries as `.txt` files.
- **Interactive web interface:** Clean, responsive layout with a light theme and purple accents.
- **Lightweight processing:** Uses sentence similarity and graph-based ranking without downloading large Transformer models.

## 🛠️ Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **NLP and text processing:** Scikit-learn (TF-IDF)
- **Similarity calculation:** Cosine similarity
- **Graph-based ranking:** NetworkX (PageRank)
- **Numerical operations:** NumPy
- **Evaluation:** ROUGE metrics using `rouge-score`

## ⚙️ How It Works

Lexora AI uses an extractive summarization approach:

1. **Input text:** The user pastes an article or document into the application.
2. **Sentence splitting:** The text is divided into individual sentences.
3. **TF-IDF vectorization:** Each sentence is represented numerically based on its word importance.
4. **Similarity calculation:** Cosine similarity measures how closely related the sentences are.
5. **Graph construction:** Sentences are represented as nodes in a graph, with similarity scores forming the connections.
6. **TextRank scoring:** PageRank assigns importance scores to the sentences based on their relationships.
7. **Summary generation:** The highest-ranked sentences are selected and returned in their original order.
8. **Output and statistics:** The application displays the summary, calculates text reduction, and allows the user to download the result.

## 📂 Project Structure


Lexora-AI/
├── app.py
├── summarizer.py
├── requirements.txt
├── evaluate.py
├── sample_articles.csv
└── README.md


*The files shown above represent the intended project structure. Include only files that are present in your repository.*


## Limitations

- TextRank selects sentences from the original text rather than generating new sentences.
- The quality of the summary depends on the input text and sentence structure.
- The current sample evaluation dataset is small.
- The application is designed as a lightweight summarization project, not a replacement for human review of critical documents.





