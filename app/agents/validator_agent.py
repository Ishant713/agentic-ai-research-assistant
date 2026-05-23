from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from app.utils.prompts import VALIDATOR_PROMPT
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)
def validator_agent(answer):
    response = llm.invoke([
        HumanMessage(content=f"{VALIDATOR_PROMPT}\n\n{answer}")
    ])

    return response.content
