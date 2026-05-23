# pyrefly: ignore [missing-import]
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.graph.workflow import app as graph_app

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/research")
def research(request: QueryRequest):
    try:
        result = graph_app.invoke({
            "query": request.query,
            "tasks": [],
            "research_outputs": [],
            "final_answer": "",
            "validation": "",
            "revision_count": 0
        })
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Backend error: {e}")

    answer = result.get("final_answer", "") if isinstance(result, dict) else ""
    if not answer:
        raise HTTPException(status_code=502, detail="Backend returned an empty answer.")

    return {
        "answer": answer
    }
