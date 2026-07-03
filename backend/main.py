from database.chat_repository import save_chat
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas.chat import ChatRequest, ChatResponse
from agents.orchestrator import process_message

from services.memory import (
    get_history,
    add_message
)


app = FastAPI(
    title="CareNavi.AI API",
    version="1.0.0",
    description="Multi-Agent Customer Support Backend"
)


# React frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Welcome to CareNavi.AI Backend 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/analyze", response_model=ChatResponse)
def analyze_chat(request: ChatRequest):

    message = request.message.lower()


    # Intent detection
    if "payment" in message:
        intent = "Billing Issue"
        priority = "High"

    elif "refund" in message:
        intent = "Refund Request"
        priority = "High"

    elif "delivery" in message:
        intent = "Delivery Issue"
        priority = "Medium"

    elif "order" in message:
        intent = "Order Issue"
        priority = "Medium"

    else:
        intent = "General Inquiry"
        priority = "Low"



    # Sentiment detection
    if any(word in message for word in [
        "angry",
        "frustrated",
        "worst",
        "bad",
        "hate",
    ]):
        sentiment = "Negative"

    else:
        sentiment = "Neutral"



    # Get previous conversation
    session_id = "user1"

    history = get_history(
        session_id
    )


    # Multi-agent + Llama + Memory
    ai_response, agent_used = process_message(
        request.message,
        history
    )


    # Save conversation
    add_message(
        session_id,
        "user",
        request.message
    )


    add_message(
        session_id,
        "assistant",
        ai_response
    )


    save_chat(
        session_id=session_id,
        user_message=request.message,
        ai_response=ai_response,
        intent=intent,
        sentiment=sentiment,
        priority=priority,
        agent=agent_used
)



    return ChatResponse(
        intent=intent,
        sentiment=sentiment,
        priority=priority,
        response=ai_response
    )