from openai import OpenAI
from typing import List, Dict
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# TODO: transform above travel plan to json data - editor js
def generate_ai_response(user_message: str, history_messages: List[Dict[str, str]]) -> str:
    # Create the list of messages including history
    messages = []
    for message in history_messages:
        messages.append({
            "role": message["role"],
            "content": message["content"]
        })
    messages.append({
        "role": "user",
        "content": user_message
    })

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return completion.choices[0].message
