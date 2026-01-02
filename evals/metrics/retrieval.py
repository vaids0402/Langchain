from typing import List


def retrieval_recall(retrieved_docs: List[str], expected_sources: List[str]) -> float:
    """
    Computes recall based on presence of expected source keywords
    in retrieved document text.

    Args:
        retrieved_docs: List of retrieved document strings
        expected_sources: Keywords expected to appear in retrieved docs

    Returns:
        Recall score between 0 and 1
    """
    if not expected_sources:
        # No context expected → retriever should return nothing
        return 1.0 if not retrieved_docs else 0.0

    combined_text = " ".join(retrieved_docs).lower()

    hits = sum(
        1 for source in expected_sources
        if source.lower() in combined_text
    )

    return hits / len(expected_sources)
