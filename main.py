from fastapi import FastAPI
from pydantic import BaseModel
from agent_service import agent

app = FastAPI()


class MessageRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: MessageRequest):
    response = agent(request.message)
    return {"response": response}
