from groq import Groq
import os

from dotenv import load_dotenv

load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



def ask_llama(role, message, history):


    messages = [
        {
            "role":"system",
            "content":f"""
You are a {role}.

Rules:
- Be helpful
- Do not mention AI
- Keep answers concise
"""
        }
    ]


    messages.extend(history)


    messages.append(
        {
            "role":"user",
            "content":message
        }
    )


    result = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )


    return result.choices[0].message.content