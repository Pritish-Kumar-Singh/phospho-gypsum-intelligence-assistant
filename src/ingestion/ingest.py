from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_experimental.text_splitter import SemanticChunker

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from src.config import VECTOR_DB_PATH


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


loader = DirectoryLoader(
    "data/raw_documents",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

documents = loader.load()


splitter = SemanticChunker(
    embeddings=embeddings
)

chunks = splitter.split_documents(documents)


vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

vectorstore.save_local(VECTOR_DB_PATH)