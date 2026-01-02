import json
from pathlib import Path

from src.search import RAGSearch
from evals.metrics.retrieval import retrieval_recall
from evals.metrics.faithfulness import faithfulness
from evals.metrics.answer_quality import judge_score

DATASET_PATH = Path(__file__).parent / "datasets" / "rag_eval.json"


def run_evaluation():
    rag = RAGSearch()
    results = []

    with open(DATASET_PATH, "r") as f:
        dataset = json.load(f)

    for example in dataset:
        question = example["question"]
        expected_answer = example["expected_answer"]
        expected_sources = example.get("expected_sources", [])

        # 🔥 EXACT MATCH
        answer, docs = rag.search_and_summarize(
            question,
            top_k=5,
            return_docs=True
        )

        eval_result = {
            "id": example["id"],
            "question": question,
            "answer": answer,
            "metrics": {
                "retrieval_recall": retrieval_recall(docs, expected_sources),
                "faithfulness": faithfulness(answer, docs),
                "answer_quality": judge_score(
                    question, answer, expected_answer
                )
            }
        }

        results.append(eval_result)

    return results


if __name__ == "__main__":
    import pprint
    pprint.pprint(run_evaluation())