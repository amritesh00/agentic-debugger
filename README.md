# 🤖 Agentic AI Coding Assistant — Intelligent Debugger

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Online-brightgreen?style=for-the-badge)](https://agentic-debugger.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> A production-grade agentic AI system that automatically detects, classifies, and resolves code errors across multiple programming languages — powered by RAG, FAISS, and LLM reasoning chains.

---

## 🔴 Live Demo

👉 **[Try it here → agentic-debugger.onrender.com](https://agentic-debugger.onrender.com)**

---

## 📌 What It Does

Paste your broken code. The system:
1. **Detects** the error type automatically (syntax, runtime, logic, etc.)
2. **Retrieves** similar past cases using vector search (RAG + FAISS)
3. **Reasons** step-by-step through the problem using an LLM agent
4. **Generates** multiple ranked fix candidates
5. **Verifies** the best fix using an AI-based verification agent
6. **Explains** the root cause in plain English

**Supported languages:** Python · JavaScript · C++

---

## ⚡ Key Results

| Metric | Result |
|---|---|
| Debugging time reduction | **30–40%** |
| Test cases validated | **150+** |
| Languages supported | **3** (Python, JS, C++) |
| Infrastructure required | **No GPU — runs on commodity cloud** |

---

## 🏗️ Architecture

```
User Input (Code + Error)
        │
        ▼
┌─────────────────┐
│  Orchestrator   │  ← Manages agent flow & state
└────────┬────────┘
         │
    ┌────┴─────┐
    ▼           ▼
┌────────┐  ┌──────────────────┐
│  RAG   │  │  Error Classifier│
│ (FAISS)│  │  Agent           │
└────┬───┘  └──────┬───────────┘
     │              │
     ▼              ▼
┌─────────────────────────────┐
│    Fix Generation Agent     │  ← LLM reasoning chain
│    (Multi-candidate)        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    AI Verification Agent    │  ← Validates best fix
└──────────────┬──────────────┘
               │
               ▼
        Final Output
   (Fix + Explanation + Root Cause)
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| AI / LLM | LLM API (reasoning chains) |
| Vector Search | FAISS (Facebook AI Similarity Search) |
| RAG Pipeline | Custom retrieval + embedding pipeline |
| Backend | Python |
| UI | Streamlit |
| Deployment | Render (cloud) |

---

## 📁 Project Structure

```
agentic-debugger/
├── agents/          # Individual AI agents (classifier, fixer, verifier)
├── orchestrator/    # Agent orchestration and workflow management
├── rag/             # RAG pipeline — embeddings, FAISS index, retrieval
├── data/            # Sample test cases and vector store data
├── ui/              # Streamlit frontend interface
├── requirements.txt
└── README.md
```

---

## 🚀 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/amritesh00/agentic-debugger.git
cd agentic-debugger

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your API key
export OPENAI_API_KEY=your_key_here   # or whichever LLM provider

# 4. Run the app
streamlit run ui/app.py
```

---

## 💡 Why This Project

Most debugging tools tell you *what* is wrong. This system tells you *why*, ranks multiple fixes, and explains the reasoning — like having a senior developer available 24/7. Built specifically to work on minimal infrastructure, making it viable for small teams without dedicated DevOps.

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

<p align="center">Built by <a href="https://github.com/amritesh00">Amritesh Bhukhmaria</a> · <a href="https://agentic-debugger.onrender.com">Live Demo</a> · <a href="https://www.linkedin.com/in/amritesh-bhukhmaria-290a5b361">LinkedIn</a></p>
