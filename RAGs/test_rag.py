from rag.loader import load_documents
from rag.splitter import split_documents
from rag.embeddings import create_vector_database
from rag.retriever import get_relevant_documents
from rag.generator import generate_answer

#load .md files
print("Loading Markdown file ...")
print("---------------------------")

documents = load_documents("uploads")

#splitting into chunks
print("Splitting document...")
print("---------------------------")
chunks = split_documents(documents)
# into db
print("Creating Vector Database...")
print("---------------------------")
create_vector_database(chunks)

print("Ready!")
print("---------------------------")
#generating answer
while True:
    try:
        question = input("\nAsk me a question (type 'exit' to quit): ")
    except EOFError:
        break

    if question.lower() == "exit":
        break

    docs = get_relevant_documents(question)
    answer = generate_answer(question, docs)

    print("\nANSWER:\n")
    print(answer)
