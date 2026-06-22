from langchain_core.runnables import (
    RunnableLambda,
    RunnablePassthrough
)

from langchain_core.prompts import ChatPromptTemplate

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

from src.config import (
    GOOGLE_API_KEY,
    VECTOR_DB_PATH
)


# ==========================================================
# Embeddings
# ==========================================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ==========================================================
# Vector Store
# ==========================================================

vectorstore = FAISS.load_local(
    VECTOR_DB_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)


# ==========================================================
# Retriever
# ==========================================================

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)


# ==========================================================
# LLM
# ==========================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.2
)


# ==========================================================
# Helper Function
# ==========================================================

def format_docs(docs):
    return "\n\n".join(
        doc.page_content
        for doc in docs
    )


# ==========================================================
# Prompt
# ==========================================================

prompt = ChatPromptTemplate.from_template(
"""
You are the Phospho-Gypsum Intelligence Assistant.

You are NOT a general chatbot.

You are an expert consultant specializing in:

- Phospho Gypsum
- IFFCO
- Sustainable Utilization
- Cement Applications
- Agriculture Applications
- Road Construction Applications
- Waste Management
- Environmental Impact
- Industrial Recommendations

Use ONLY the provided context.

Question:
{question}

Context:
{context}

If information is not available in the context, clearly state:

"Information not found in the available knowledge base."

Always provide the answer in the following format:

## Summary

Provide a concise answer.

## Detailed Explanation

Provide detailed evidence-based explanation.

## Recommendation

Provide practical recommendations.

## Sources Used

List the source documents used.
"""
)


# ==========================================================
# RAG Inputs
# ==========================================================

rag_inputs = {
    "question": RunnablePassthrough(),
    "context": retriever | RunnableLambda(format_docs)
}


# ==========================================================
# Main Chain
# ==========================================================

rag_chain = (
    rag_inputs
    | prompt
    | llm
)