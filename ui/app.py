import streamlit as st
from orchestrator.controller import run_debugger
from rag.vector_store import load_documents

st.title("Agentic AI Code Debugging Assistant")

load_documents()

code = st.text_area("Paste your code")

error = st.text_area("Paste error message")

if st.button("Analyze Code"):

    explanation,fix,verification = run_debugger(code,error)

    st.subheader("Error Analysis")
    st.write(explanation)

    st.subheader("Suggested Fix")
    st.code(fix)

    st.subheader("Verification")
    st.write(verification)