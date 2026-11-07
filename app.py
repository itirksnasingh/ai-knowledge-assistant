"""Initial Streamlit landing page for AI Knowledge Assistant.

The application is a scaffold. It deliberately does not claim that planned
modelling, evaluation, or deployment features are implemented.
"""
import streamlit as st

st.set_page_config(page_title="AI Knowledge Assistant", page_icon="🧪", layout="wide")
st.title("AI Knowledge Assistant")
st.caption("Evidence-grounded document intelligence and question answering")
st.warning("Development scaffold: core workflows are being implemented.")

st.subheader("Research question")
st.write("How do lexical, dense, and hybrid retrieval strategies compare on a defined document collection, and how should a question-answering system behave when retrieved evidence is insufficient?")

st.subheader("Planned methodology")
for item in ["Document ingestion with page/section metadata", "BM25 lexical retrieval baseline", "Dense retrieval using sentence embeddings and FAISS", "Hybrid retrieval combining lexical and semantic signals", "Optional reranking experiment", "Evidence-linked answer generation with source references", "Abstention policy for insufficient or conflicting evidence"]:
    st.write("• " + item)

st.subheader("Project status")
st.write("Scope defined · Implementation in progress · Evaluation pending · Deployment pending")
