from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from app.utils.prompts import SUMMARY_PROMPT
from dotenv import load_dotenv
load_dotenv()


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

MAX_OUTPUTS = 2
MAX_OUTPUT_LENGTH = 800
MAX_SUMMARY_INPUT = 2400


def _truncate(text, max_chars=MAX_OUTPUT_LENGTH):
    if not text:
        return ""
    return text if len(text) <= max_chars else text[:max_chars].rsplit(" ", 1)[0] + "..."


def summarizer_agent(outputs, feedback=None):
    safe_outputs = [
        _truncate(output) for output in outputs[:MAX_OUTPUTS] if output and output.strip()
    ]
    if not safe_outputs:
        return "Unable to summarize because no research outputs were produced."

    combined = "\n\n".join(safe_outputs)
    combined = combined if len(combined) <= MAX_SUMMARY_INPUT else combined[:MAX_SUMMARY_INPUT].rsplit(" ", 1)[0] + "..."

    prompt = f"{SUMMARY_PROMPT}\n\n{combined}"
    if feedback and "APPROVED" not in feedback:
        prompt += f"\n\nPrevious attempt was rejected with feedback:\n{feedback}\nPlease revise the summary to address this feedback."

    try:
        response = llm.invoke([
            HumanMessage(content=prompt)
        ])
        return response.content
    except Exception as e:
        return f"[Summarizer failed: {e}]"
