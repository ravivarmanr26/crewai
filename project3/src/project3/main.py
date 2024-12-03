#!/usr/bin/env python
import sys
import warnings
import logging
from fastapi import FastAPI
from pydantic import BaseModel
from crew import JobAssistanceCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

app = FastAPI()

class JobInput(BaseModel):
    job_role: str
    company_name: str

@app.post("/run")
def run(input_data: JobInput):
    """
    Run the crew with input from FastAPI.
    """
    inputs = {
        'job_role': input_data.job_role,
        'company_name': input_data.company_name
    }
    JobAssistanceCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)