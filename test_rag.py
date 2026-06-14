from src.retrieval.rag_chain import ask_question


question = """
Can phospho gypsum be used in road construction?
"""


answer = ask_question(question)

print(answer)