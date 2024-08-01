from openai import OpenAI
from typing import List, Dict

import os
import json

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

def extract_json_from_ai_response(response: str) -> Dict:
    # Extract and transform JSON data from AI response
    json_start = '```json'
    json_end = '```'
    try:
        start = response.index(json_start)
        end = response.rindex(json_end)
        json_str = response[start+len(json_start):end]
        json_data = json.loads(json_str)
        return json_data
    except (ValueError, json.JSONDecodeError) as e:
        raise ValueError("Failed to extract JSON from AI response") from e