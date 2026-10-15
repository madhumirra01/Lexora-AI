import re
import time

import networkx as nx
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def split_sentences(text):
    """Split text into individual sentences."""
    return [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+", text.strip())
        if sentence.strip()
    ]


def textrank_summarize(text, sentence_count=3):
    """Generate an extractive summary using the TextRank algorithm."""
    sentences = split_sentences(text)

    if not sentences:
        return ""

    if len(sentences) <= sentence_count:
        return " ".join(sentences)

    try:
        vectorizer = TfidfVectorizer(stop_words="english")
        sentence_vectors = vectorizer.fit_transform(sentences)
        similarity_matrix = cosine_similarity(sentence_vectors)
    except ValueError:
        return " ".join(sentences[:sentence_count])

    np.fill_diagonal(similarity_matrix, 0)

    graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(graph, weight="weight", max_iter=200)

    ranked_indices = sorted(
        scores, key=scores.get, reverse=True
    )

    selected_indices = sorted(ranked_indices[:sentence_count])

    return " ".join(sentences[i] for i in selected_indices)


def summarize(text, sentence_count=3):
    """Summarize text and return the summary and processing time."""
    if not text or not text.strip():
        raise ValueError("Please provide some text.")

    if sentence_count < 1:
        raise ValueError("Sentence count must be at least 1.")

    start = time.perf_counter()
    summary = textrank_summarize(text, sentence_count)
    elapsed = time.perf_counter() - start

    return summary, elapsed