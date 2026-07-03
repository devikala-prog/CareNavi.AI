from services.llama_service import ask_llama


def billing_agent(message, history):

    return ask_llama(
        "Billing and Payment Specialist",
        message,
        history
    )