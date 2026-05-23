from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from app.tools.web_search import search_web
from app.tools.rag_tool import retrieve_context
from app.utils.prompts import RESEARCH_PROMPT
from dotenv import load_dotenv
load_dotenv()


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

MAX_CONTEXT_CHARS = 2000
MAX_WEB_RESULTS = 2
MAX_WEB_CONTENT_CHARS = 800


def _truncate(text, max_chars=MAX_CONTEXT_CHARS):
    if not text:
        return ""
    return text if len(text) <= max_chars else text[:max_chars].rsplit(" ", 1)[0] + "..."


def researcher_agent(task):
    web_results = search_web(task)[:MAX_WEB_RESULTS]
    rag_context = _truncate(retrieve_context(task))

    combined_web = "\n".join([
        _truncate(result.get("content", ""), max_chars=MAX_WEB_CONTENT_CHARS)
        for result in web_results
    ])

    prompt = f'''
    {RESEARCH_PROMPT}

    Task:
    {task}

    Context:
    {rag_context}

    Web:
    {combined_web}
    '''

    try:
        response = llm.invoke([
            HumanMessage(content=prompt)
        ])
        return response.content
    except Exception as e:
        return f"[Researcher failed: {e}]"
