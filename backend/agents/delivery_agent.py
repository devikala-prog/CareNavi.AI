from services.llama_service import ask_llama


def delivery_agent(message, history):

    return ask_llama(
        "Delivery and Order Specialist",
        message,
        history
    )