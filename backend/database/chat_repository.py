from datetime import datetime
from database.mongodb import chat_collection


def save_chat(
    session_id,
    user_message,
    ai_response,
    intent,
    sentiment,
    priority,
    agent
):
    document = {
        "session_id": session_id,
        "user_message": user_message,
        "ai_response": ai_response,
        "intent": intent,
        "sentiment": sentiment,
        "priority": priority,
        "agent": agent,
        "timestamp": datetime.utcnow()
    }

    result = chat_collection.insert_one(document)

    return str(result.inserted_id)


def get_chat_history(session_id):
    chats = chat_collection.find(
        {"session_id": session_id}
    ).sort("timestamp", 1)

    return list(chats)


def get_total_chat_count():
    return chat_collection.count_documents({})