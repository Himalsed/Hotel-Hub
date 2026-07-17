import os

from dotenv import load_dotenv

load_dotenv()

_LLM_CACHE = None


def _get_llm():
    global _LLM_CACHE
    if _LLM_CACHE is None:
        try:
            from langchain_huggingface import HuggingFaceEndpoint

            model_name = os.getenv("LLAMA_MODEL") or "microsoft/Phi-3.5-mini-instruct"
            token = os.getenv("HF_TOKEN")
            _LLM_CACHE = HuggingFaceEndpoint(
                repo_id=model_name,
                task="text-generation",
                max_new_tokens=300,
                temperature=0,
                huggingfacehub_api_token=token,
            )
        except Exception:
            _LLM_CACHE = None
    return _LLM_CACHE


def _build_fallback_answer(question, documents):
    if not documents:
        return "I could not find enough hotel policy."

    context = "\n".join(
        getattr(doc, "page_content", "")
        for doc in documents
        if getattr(doc, "page_content", "")
    )

    excerpt = " ".join(part.strip() for part in context.splitlines() if part.strip())[:300]

    if not excerpt:
        return "I could not find enough hotel policy."

    return excerpt


def generate_answer(question, documents):
    context = "\n".join(
        getattr(doc, "page_content", "")
        for doc in documents
        if getattr(doc, "page_content", "")
    )

    prompt = f"""
You are a helpful hotel assistant.

Answer ONLY from the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    try:
        llm = _get_llm()
        if llm is None:
            raise RuntimeError("LLM provider unavailable")
        response = llm.invoke(prompt)
        return getattr(response, "content", str(response))
    except Exception:
        return _build_fallback_answer(question, documents)