from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from app.utils.prompts import PLANNER_PROMPT


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)
def planner_agent(query):
    response = llm.invoke([
        HumanMessage(content=f"{PLANNER_PROMPT}\n\n{query}")
    ])

    tasks = []
    for line in response.content.split("\n"):
        line = line.strip()
        if not line:
            continue
        # Strip common markdown bullet points and numbering
        if line.startswith(("-", "*", "•")):
            line = line[1:].strip()
        elif "." in line and line.split(".", 1)[0].isdigit():
            line = line.split(".", 1)[1].strip()
        
        if line:
            tasks.append(line)
            
    return tasks[:3]