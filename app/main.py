from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from agents.crew import run_crew

app = FastAPI(title="CrewAI API", description="FastAPI backend for CrewAI agent runs")


class RunRequest(BaseModel):
    topic: str


class RunResponse(BaseModel):
    result: str


@app.get("/")
def root():
    return {"status": "ok", "message": "CrewAI API is running"}


@app.post("/run", response_model=RunResponse)
def run(request: RunRequest):
    if not request.topic.strip():
        raise HTTPException(status_code=400, detail="Topic cannot be empty")
    result = run_crew(request.topic.strip())
    return RunResponse(result=result)
