
import os
import pandas as pd
from rouge_score import rouge_scorer

from summarizer import summarize


def main():
    data = pd.read_csv("sample_articles.csv")

    required_columns = {
        "article_id",
        "title",
        "text",
        "reference_summary",
    }

    if not required_columns.issubset(data.columns):
        raise ValueError(
            f"Dataset must contain {required_columns}"
        )

    scorer = rouge_scorer.RougeScorer(
        ["rouge1", "rouge2", "rougeL"],
        use_stemmer=True,
    )

    rows = []

    for _, item in data.iterrows():
        prediction, elapsed = summarize(
            str(item["text"]),
            method="TextRank",
            sentence_count=3,
        )

        scores = scorer.score(
            str(item["reference_summary"]),
            prediction,
        )

        rows.append({
            "article_id": item["article_id"],
            "title": item["title"],
            "generated_summary": prediction,
            "reference_summary": item["reference_summary"],
            "rouge1_f1": scores["rouge1"].fmeasure,
            "rouge2_f1": scores["rouge2"].fmeasure,
            "rougeL_f1": scores["rougeL"].fmeasure,
            "processing_seconds": elapsed,
        })

    results = pd.DataFrame(rows)
    os.makedirs("results", exist_ok=True)

    results.to_csv(
        "results/evaluation_results.csv",
        index=False,
    )

    print("\nEvaluation results:")
    print(
        results[
            ["title", "rouge1_f1", "rouge2_f1", "rougeL_f1"]
        ].to_string(index=False)
    )

    print("\nAverage ROUGE F1 scores:")
    print(
        results[
            ["rouge1_f1", "rouge2_f1", "rougeL_f1"]
        ].mean().round(4)
    )

    print("\nResults saved to results/evaluation_results.csv")


if __name__ == "__main__":
    main()
