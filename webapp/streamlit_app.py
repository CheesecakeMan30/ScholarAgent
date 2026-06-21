"""
Simple Streamlit interface for ScholarAgent.
"""

import streamlit as st

from app.ingest import ingest_folder
from app.embeddings import build_index
from app.agent_pipeline import run_pipeline

st.title("ScholarAgent")

st.write(
    "Upload PDF files into the demo/demo_papers folder and ask questions about them."
)

if st.button("Build Index"):

    docs = ingest_folder("demo/demo_papers")

    st.write(f"Loaded {len(docs)} document(s).")

    vectorstore = build_index(docs)

    st.session_state["vectorstore"] = vectorstore

    st.success("Vector database created successfully!")

query = st.text_input(
    "Enter your research question:"
)

if st.button("Run Agent"):

    if "vectorstore" not in st.session_state:
        st.error("Please build the index first.")
    else:

        answer = run_pipeline(
            query=query,
            vectorstore=st.session_state["vectorstore"]
        )

        st.subheader("Results")

        st.write(answer)