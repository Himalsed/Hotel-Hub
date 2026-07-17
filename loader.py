from langchain_community.document_loaders import DirectoryLoader, TextLoader

def load_documents(folder_path="uploads"):
    """
    Load all Markdown files from the uploads folder.
    """
    loader = DirectoryLoader(
        folder_path,
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )

    documents = loader.load()
    return documents