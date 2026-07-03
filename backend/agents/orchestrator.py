from agents.billing_agent import billing_agent
from agents.delivery_agent import delivery_agent
from agents.support_agent import support_agent


def process_message(message, history):

    text = message.lower()

    if "payment" in text or "refund" in text:
        response = billing_agent(message, history)
        return response, "Billing Agent"

    elif "delivery" in text or "order" in text:
        response = delivery_agent(message, history)
        return response, "Delivery Agent"

    else:
        response = support_agent(message, history)
        return response, "Support Agent"