import os
from pathlib import Path

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

_EMBEDDINGS_CACHE = None
_VECTOR_DB_CACHE = None


def get_embeddings():
    global _EMBEDDINGS_CACHE
    if _EMBEDDINGS_CACHE is None:
        _EMBEDDINGS_CACHE = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    return _EMBEDDINGS_CACHE


def _get_persist_directory(persist_directory=None):
    if persist_directory is not None:
        return str(Path(persist_directory).expanduser().resolve())

    base_dir = Path(__file__).resolve().parent.parent
    return str((base_dir / "vector_db").resolve())


def create_vector_database(chunks, persist_directory=None):
    global _VECTOR_DB_CACHE

    embeddings = get_embeddings()
    persist_dir = _get_persist_directory(persist_directory)
    persist_path = Path(persist_dir)

    if _VECTOR_DB_CACHE is not None:
        return _VECTOR_DB_CACHE

    if persist_path.exists() and any(persist_path.iterdir()):
        _VECTOR_DB_CACHE = Chroma(
            persist_directory=persist_dir,
            embedding_function=embeddings
        )
        return _VECTOR_DB_CACHE

    _VECTOR_DB_CACHE = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    return _VECTOR_DB_CACHE