from backend.services.vectorstore import VectorStore

# 🔒 FINAL SWITCH
LOCAL_MODE = True  # keep True for now (stable + offline)


def answer_question(chunks, question):
    """
    Hybrid RAG:
    - Local mode: context-based deterministic answer
    - LLM mode: plug OpenAI later without changing API
    """

    vectorstore = VectorStore(chunks)
    relevant_chunks = vectorstore.search(question, top_k=5)

    context = "\n\n".join(
        [f"File: {c['file_path']}\n{c['text']}" for c in relevant_chunks]
    )

    if LOCAL_MODE:
        return local_reasoning(context, question)

    else:
        # 🔌 Future: OpenAI / Gemini goes here
        raise NotImplementedError("LLM mode not enabled yet")


def local_reasoning(context, question):
    """
    Deterministic reasoning for code explanation & debugging
    """

    response = f"""
QUESTION:
{question}

RELEVANT CODE CONTEXT:
{context}

EXPLANATION:
The above files and code sections are most relevant to your question.
Review how functions, imports, and APIs interact in these files.
"""

    return response.strip()
