from typing import List


def faithfulness(answer: str, retrieved_docs: List[str]) -> float:
    """
    Measures how much of the answer is grounded in retrieved documents.

    Strategy:
    - Split answer into sentences
    - Check if each sentence appears in retrieved context

    Args:
        answer: Model-generated answer
        retrieved_docs: Retrieved document text

    Returns:
        Faithfulness score between 0 and 1
    """
    if not answer.strip():
        return 0.0

    if not retrieved_docs:
        # If no docs were retrieved, any answer is hallucinated
        return 0.0

    context = " ".join(retrieved_docs)

    sentences = [
        s.strip() for s in answer.split(".")
        if s.strip()
    ]

    if not sentences:
        return 0.0

    supported = sum(
        1 for sentence in sentences
        if sentence in context
    )

    return supported / len(sentences)
