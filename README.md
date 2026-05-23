Agentic AI Research Assistant

An advanced Agentic AI Research Assistant built using LangGraph, LangChain, ChromaDB, Groq LLM, Tavily Search, and Streamlit.
This project demonstrates a multi-agent AI workflow capable of planning, researching, validating, and summarizing information autonomously.

🚀 Live Demo

🌐 Live App:
Agentic AI Research Assistant Live Demo

📌 Features
Multi-Agent AI Architecture
Research Planning Agent
Web Search Integration (Tavily API)
Summarization Agent
Validation Agent
Vector Memory using ChromaDB
LangGraph Workflow Orchestration
Streamlit Interactive UI
FastAPI Backend Support
Retrieval-Augmented Generation (RAG)
Persistent Vector Storage
🧠 Tech Stack
Frontend
Streamlit
Backend
FastAPI
Uvicorn
AI Frameworks
LangChain
LangGraph
LLM
Groq API
Vector Database
ChromaDB
Embeddings
HuggingFace Sentence Transformers
Search Tool
Tavily Search API
📂 Project Structure
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
└── README.md
⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/Ishant713/agentic-ai-research-assistant.git
cd agentic-ai-research-assistant
2️⃣ Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
📦 Install Dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file in the root directory.

TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
▶️ Run Streamlit App
streamlit run app/ui/streamlit_app.py
▶️ Run FastAPI Backend
python -m uvicorn app.api.main:app --reload
🧩 Agent Workflow

The system follows an Agentic Workflow:

Planner Agent creates research tasks
Researcher Agent gathers information
Validator Agent validates outputs
Summarizer Agent generates final response
Memory module stores embeddings in ChromaDB
📸 Screenshots
Streamlit UI
Interactive research query interface
Multi-agent response generation
Real-time research workflow
🌟 Future Improvements
Multi-modal support
PDF research upload
Citation generation
Conversation memory
Autonomous task execution
Docker deployment
Authentication system
👨‍💻 Author
Ishan Dhakad
Information Security Student
AI & Agentic Systems Enthusiast
Developer of AI Research Workflows

GitHub:
Ishan Dhakad GitHub

📜 License

This project is developed for educational and research purposes.
