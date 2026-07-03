from services.llama_service import ask_llama


def support_agent(message, history):

    return ask_llama(
        "General Customer Support Specialist",
        message,
        history
    )