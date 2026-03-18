import streamlit as st
import sys
import os

# Fix import paths for Render
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from orchestrator.controller import run_debugger
from rag.vector_store import load_documents

# Page config (optional but looks better)
st.set_page_config(page_title="AI Code Debugger", page_icon="🤖")

st.title("🤖 Agentic AI Code Debugging Assistant")

# Cache heavy loading (IMPORTANT FIX)
@st.cache_resource
def init():
    load_documents()

init()

# UI Inputs
code = st.text_area("💻 Paste your code here", height=200)
error = st.text_area("⚠️ Paste error message here", height=100)

# Button
if st.button("Analyze Code"):
    
    if not code or not error:
        st.warning("Please provide both code and error message.")
    else:
        with st.spinner("Analyzing... ⏳"):

            try:
                explanation, ranked, verification = run_debugger(code, error)

                # Error Analysis
                st.subheader("Error Analysis")
                st.write(explanation)

                # Fixes
                st.subheader("🛠️ Suggested Fixes")

                for i, (fix, score) in enumerate(ranked[:3]):
                    st.markdown(f"### 🔹 Fix {i+1} (Confidence: {score})")
                    st.code(fix)

                # Verification
                st.subheader("Verification")
                st.write(verification)

            except Exception as e:
                st.error(f"Error occurred: {str(e)}")