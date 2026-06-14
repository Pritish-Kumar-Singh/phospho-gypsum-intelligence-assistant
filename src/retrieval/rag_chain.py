from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

from src.config import GOOGLE_API_KEY, VECTOR_DB_PATH
from src.prompts import SYSTEM_PROMPT


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.load_local(
    VECTOR_DB_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 8}
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.2
)


def ask_question(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    sources = sorted(
        set(
            doc.metadata.get("source_file", "Unknown")
            for doc in docs
        )
    )

    prompt = f"""
{SYSTEM_PROMPT}

CONTEXT:
{context}

QUESTION:
{question}
"""

    response = llm.invoke(prompt)

    source_text = "\n".join(
        f"- {source}"
        for source in sources
    )

    return f"""
{response.content}

---

### Retrieved Source Documents

{source_text}
"""