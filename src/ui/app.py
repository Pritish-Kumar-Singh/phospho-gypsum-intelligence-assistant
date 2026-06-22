import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

from src.retrieval.rag_chain import rag_chain

st.set_page_config(
    page_title="Phospho-Gypsum Intelligence Assistant",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Phospho-Gypsum Intelligence Assistant")

st.markdown(
"""
AI-Powered Knowledge and Recommendation System for Sustainable Phospho-Gypsum Utilization
"""
)

st.divider()

question = st.text_area(
    "Enter Your Question",
    height=150
)

if st.button("Generate Answer"):

    if question:

        with st.spinner("Analyzing documents and generating recommendations..."):

            response = rag_chain.invoke(question)
            answer = response.content

        st.success("Analysis Complete")

        st.markdown(answer)