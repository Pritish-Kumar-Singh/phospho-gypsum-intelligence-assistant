

from src.retrieval.rag_chain import rag_chain

response = rag_chain.invoke(
    "What are the applications of phospho gypsum?"
)

print(response.content)