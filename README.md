# 🏨 Hotel Knowledge Hub

Hotel Knowledge Hub is an AI-powered chatbot that answers hotel-related questions using Retrieval-Augmented Generation (RAG). Instead of relying only on an LLM, it retrieves relevant information from hotel knowledge documents and generates accurate, context-aware responses.

## Features

- 📄 Markdown-based knowledge base
- 🔍 Semantic search with ChromaDB
- 🤖 Hugging Face embeddings
- 🧠 LangChain RAG pipeline
- 💬 Interactive command-line chatbot
- ⚡ Fast document retrieval
- 🏨 Supports hotel policies, restaurant information, staff guidelines, and FAQs

## Tech Stack

- Python
- LangChain
- ChromaDB
- Hugging Face Embeddings
- Markdown (.md)
- LLM

## Project Structure

```
Hotel-Knowledge-Hub/
│── rag/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── retriever.py
│   └── generator.py
│
├── uploads/
│   ├── hotel_policy.md
│   ├── staff_policy.md
│   └── restaurant_policy.md
│
├── chroma_db/
├── test_rag.py
├── requirements.txt
└── README.md
```

## Example Questions

- What time is check-in?
- What is the cancellation policy?
- What are the restaurant opening hours?
- What is the staff dress code?
- Does the hotel provide airport pickup?

## Future Improvements

- Web interface with Streamlit or Flask
- Multi-language support
- PDF and DOCX document support
- Conversation memory
- Admin dashboard for document management