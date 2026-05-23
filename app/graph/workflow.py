from typing import TypedDict, List
from langgraph.graph import StateGraph, END

from app.agents.planner_agent import planner_agent
from app.agents.researcher_agent import researcher_agent
from app.agents.summarizer_agent import summarizer_agent
from app.agents.validator_agent import validator_agent

class AgentState(TypedDict):
    query: str
    tasks: List[str]
    research_outputs: List[str]
    final_answer: str
    validation: str
    revision_count: int

def planning_node(state):
    tasks = [task.strip() for task in planner_agent(state["query"]) if task.strip()]
    return {
        "tasks": tasks
    }

def research_node(state):
    outputs = []

    for task in state["tasks"]:
        try:
            outputs.append(researcher_agent(task))
        except Exception as e:
            outputs.append(str(e))

    return {
        "research_outputs": outputs
    }

def summarizer_node(state):
    validation_feedback = state.get("validation", "")
    final_answer = summarizer_agent(state["research_outputs"], validation_feedback)
    if not final_answer or not final_answer.strip():
        final_answer = "Unable to generate a summary from the research outputs."

    revision_count = state.get("revision_count", 0) + 1

    return {
        "final_answer": final_answer,
        "revision_count": revision_count
    }

def validator_node(state):
    return {
        "validation": validator_agent(state["final_answer"])
    }

def router(state):
    if "APPROVED" in state["validation"] or state.get("revision_count", 0) >= 3:
        return END

    return "summarizer"

workflow = StateGraph(AgentState)

workflow.add_node("planner", planning_node)
workflow.add_node("researcher", research_node)
workflow.add_node("summarizer", summarizer_node)
workflow.add_node("validator", validator_node)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "researcher")
workflow.add_edge("researcher", "summarizer")
workflow.add_edge("summarizer", "validator")

workflow.add_conditional_edges(
    "validator",
    router,
    {
        "summarizer": "summarizer",
        END: END
    }
)

app = workflow.compile()
