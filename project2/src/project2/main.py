#I'll help you create a FastAPI endpoint to send inputs to your CrewAI agents. Here's how you can modify your code to integrate FastAPI

#!/usr/bin/env python
import sys
import warnings
from fastapi import FastAPI
from pydantic import BaseModel
from crew import Project2

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

app = FastAPI()

class TopicInput(BaseModel):
    topic: str

@app.post("/run-crew")
async def run_crew(topic_input: TopicInput):
    """
    API endpoint to run the crew with given input
    """
    inputs = {
        'topic': topic_input.topic
    }
    result = Project2().crew().kickoff(inputs=inputs)
    return {"result": result}

# Keep the original run function for local testing
# def run():
#     """
#     Run the crew locally.
#     """
#     inputs = {
#         'topic': 'rag'
#     }
#     Project2().crew().kickoff(inputs=inputs)

# run()
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)