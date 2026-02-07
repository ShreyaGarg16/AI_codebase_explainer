"""from backend.services.vectorstore import get_vectorstore

def answer_question(chunks, question):
    if not chunks:
        return "No code files found."

    vectorstore = get_vectorstore(chunks)
    relevant_chunks = vectorstore.search(question)

    answer = "Based on the codebase:\n\n"

    for c in relevant_chunks:
        answer += f"File: {c['file_path']}\n"
        answer += c["text"][:800]  # avoid dumping huge files
        answer += "\n\n"

    return answer

from backend.services.vectorstore import VectorStore
from backend.services.llm import call_llm

def answer_question(chunks, question):
    if not chunks:
        return "No code files were found."

    vectorstore = VectorStore(chunks)
    relevant_chunks = vectorstore.search(question, top_k=1)

    context = "\n\n".join(
        f"File: {c['file_path']}\n{c['text'][:300]}"
        for c in relevant_chunks
    )

    prompt = f
You are a codebase explainer.

Answer the question using ONLY the context below.

CONTEXT:
{context}

QUESTION:
{question}

Give a clear, short answer.


    return {
        "answer": call_llm(prompt),
        "source": context
    }
"""
from backend.services.llm import call_llm


def answer_question(chunks, question: str):
    """
    Simple and stable RAG:
    1. Find relevant chunks using keyword match
    2. Build a short context
    3. Ask LLM using that context
    """

    if not chunks:
        return {
            "error": "No code chunks available. Please ingest a repository first."
        }

    question_lower = question.lower()
    relevant = []

    # --- Step 1: naive but reliable retrieval ---
    for c in chunks:
        if question_lower in c["text"].lower():
            relevant.append(c)

    # fallback: take first few chunks if nothing matched
    if not relevant:
        relevant = chunks[:3]

    # --- Step 2: build context ---
    context_parts = []
    for c in relevant[:3]:
        context_parts.append(
            f"File: {c['file_path']}\n{c['text'][:300]}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are a codebase explainer.

Answer the question using ONLY the code context below.

CODE CONTEXT:
{context}

QUESTION:
{question}

Give a clear and concise answer.
"""

    # --- Step 3: call LLM (Ollama / later API) ---
    try:
        answer = call_llm(prompt)
    except Exception as e:
        # LLM fallback (VERY important for stability)
        return {
            "question": question,
            "answer": "LLM not available. Showing relevant code instead.",
            "source": context,
            "error": str(e)
        }

    return {
        "question": question,
        "answer": answer,
        "source": context
    }
