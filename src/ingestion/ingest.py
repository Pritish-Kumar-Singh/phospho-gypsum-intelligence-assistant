import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


load_dotenv()


RAW_DOCS_PATH = "data/raw_documents"
VECTOR_DB_PATH = "data/vector_store"


def load_documents():

    documents = []

    pdf_files = [
        file
        for file in os.listdir(RAW_DOCS_PATH)
        if file.endswith(".pdf")
    ]

    print(f"\nFound {len(pdf_files)} PDFs\n")

    for pdf in pdf_files:

        pdf_path = os.path.join(RAW_DOCS_PATH, pdf)

        print(f"Loading: {pdf}")

        loader = PyPDFLoader(pdf_path)

        docs = loader.load()

        for doc in docs:
            doc.metadata["source_file"] = pdf

        documents.extend(docs)

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"\nCreated {len(chunks)} chunks\n")

    return chunks


def create_vector_db(chunks):

    print("Loading embedding model...\n")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating FAISS index...\n")

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local(VECTOR_DB_PATH)

    print("\nVector database created successfully!\n")


def main():

    print("\n===== PHOSPHO-GYPSUM INGESTION =====\n")

    documents = load_documents()

    chunks = split_documents(documents)

    create_vector_db(chunks)

    print("Done.")


if __name__ == "__main__":
    main()