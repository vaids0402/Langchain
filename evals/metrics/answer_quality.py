from langchain_groq import ChatGroq
import os


def judge_score(question: str, answer: str, expected_answer: str) -> int:
    """
    Uses an LLM to judge answer correctness.

    Scoring scale:
    1 = incorrect / hallucinated
    3 = partially correct
    5 = fully correct

    Args:
        question: Original question
        answer: Model-generated answer
        expected_answer: Reference answer

    Returns:
        Integer score from 1 to 5
    """
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant",
        temperature=0
    )

    prompt = f"""
You are evaluating a student's answer.

Question:
{question}

Expected Answer:
{expected_answer}

Student Answer:
{answer}

Rate the student's answer from 1 to 5:
- 1 = incorrect or hallucinated
- 3 = partially correct
- 5 = fully correct

Return ONLY the number.
"""

    response = llm.invoke([prompt]).content.strip()

    try:
        score = int(response)
        return min(max(score, 1), 5)
    except ValueError:
        return 1
