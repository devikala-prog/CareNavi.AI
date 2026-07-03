from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    intent: str
    sentiment: str
    priority: str
    response: str