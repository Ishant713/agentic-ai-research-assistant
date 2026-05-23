# Agentic AI Research Assistant

An advanced **Agentic AI Research Assistant** built using **LangGraph, LangChain, ChromaDB, Groq LLM, Tavily Search, and Streamlit**.  
This project demonstrates a multi-agent AI workflow capable of planning, researching, validating, and summarizing information autonomously.

---

# 🚀 Live Demo

🌐 Live App:  
https://agentic-ai-research-assistant-s3dcbkuhvvxap3bb9azn3p.streamlit.app/

---

# 📌 Features

- Multi-Agent AI Architecture
- Research Planning Agent
- Web Search Integration (Tavily API)
- Summarization Agent
- Validation Agent
- Vector Memory using ChromaDB
- LangGraph Workflow Orchestration
- Streamlit Interactive UI
- FastAPI Backend Support
- Retrieval-Augmented Generation (RAG)
- Persistent Vector Storage
- Autonomous Research Workflow

---

# 🧠 Tech Stack

## Frontend
- Streamlit

## Backend
- FastAPI
- Uvicorn

## AI Frameworks
- LangChain
- LangGraph

## LLM
- Groq API

## Vector Database
- ChromaDB

## Embeddings
- HuggingFace Sentence Transformers

## Search Tool
- Tavily Search API

---

# 📂 Project Structure

```bash
agentic-ai-research-assistant/
│
├── app/
│   ├── agents/
│   │   ├── planner_agent.py
│   │   ├── researcher_agent.py
│   │   ├── summarizer_agent.py
│   │   └── validator_agent.py
│   │
│   ├── api/
│   │   └── main.py
│   │
│   ├── graph/
│   │   └── workflow.py
│   │
│   ├── memory/
│   │   └── vector_store.py
│   │
│   ├── tools/
│   │   ├── rag_tool.py
│   │   └── web_search.py
│   │
│   ├── ui/
│   │   └── streamlit_app.py
│   │
│   └── utils/
│       └── prompts.py
│
├── chroma_db/
├── data/
├── requirements.txt
├── packages.txt
├── runtime.txt
├── .streamlit/
│   └── config.toml
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Ishant713/agentic-ai-research-assistant.git
cd agentic-ai-research-assistant
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run Streamlit App

```bash
streamlit run app/ui/streamlit_app.py
```

---

# ▶️ Run FastAPI Backend

```bash
python -m uvicorn app.api.main:app --reload
```

---

# 🧩 Agent Workflow

The system follows an intelligent multi-agent workflow:

1. Planner Agent creates research tasks
2. Researcher Agent gathers information from web sources
3. Validator Agent verifies the generated outputs
4. Summarizer Agent creates the final summarized response
5. Memory module stores embeddings in ChromaDB for retrieval

---

# 🔄 Workflow Architecture

```text
User Query
    ↓
Planner Agent
    ↓
Researcher Agent
    ↓
Validator Agent
    ↓
Summarizer Agent
    ↓
Final Response
```

---

# 📸 Application Preview

## Streamlit UI

- Interactive research query interface
- Real-time AI research generation
- Multi-agent orchestration
- Research summarization
- Autonomous workflow execution

---

# 🌟 Future Improvements

- Multi-modal AI support
- PDF and document upload research
- Citation generation
- Long-term conversational memory
- Autonomous task scheduling
- Docker deployment
- Authentication system
- Research history tracking

---

# 🛠 Deployment

This project is deployed using:

- GitHub
- Streamlit Community Cloud

---

# 👨‍💻 Author

## Ishan Dhakad

- Information Security Student
- AI & Agentic Systems Enthusiast
- Developer of AI Research Workflows

GitHub:  
https://github.com/Ishant713

---

# 📜 License

This project is developed for educational and research purposes.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
