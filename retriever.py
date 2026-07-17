from langchain_chroma import Chroma

from rag.embeddings import _get_persist_directory, get_embeddings

_VECTOR_DB_CACHE = None


def _get_vector_db():
    global _VECTOR_DB_CACHE
    if _VECTOR_DB_CACHE is None:
        _VECTOR_DB_CACHE = Chroma(
            persist_directory=_get_persist_directory(),
            embedding_function=get_embeddings()
        )
    return _VECTOR_DB_CACHE


def get_relevant_documents(question):
    try:
        vector_db = _get_vector_db()
        return vector_db.similarity_search(question, k=3)
    except Exception:
        return []