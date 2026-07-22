# 🏨 Hotel Knowledge Hub

Hotel Knowledge Hub is an AI-powered chatbot that answers hotel-related questions using Retrieval-Augmented Generation (RAG). Instead of relying only on an LLM, it retrieves relevant information from hotel knowledge documents and generates accurate, context-aware responses.

# 🛠️ Tech Stack

### Programming Language
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### AI & Retrieval
![RAG](https://img.shields.io/badge/RAG-Retrieval--Augmented--Generation-blue?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-Agent_Framework-1C3C3C?style=for-the-badge)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Embeddings-yellow?style=for-the-badge&logo=huggingface)

### Vector Database
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Database-5B21B6?style=for-the-badge)

### Data Source
![Markdown](https://img.shields.io/badge/Markdown-Knowledge_Base-000000?style=for-the-badge&logo=markdown)

### AI Model
![LLM](https://img.shields.io/badge/LLM-Context_Aware_Responses-orange?style=for-the-badge)

### Development Tools
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

### Operating Systems
- 🍎 macOS
- 🪟 Windows
- 🐧 Linux




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
