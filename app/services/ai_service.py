from openai import OpenAI
from typing import List, Dict

import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to truncate message history if it exceeds the token limit
def truncate_message_history(history_messages: List[Dict[str, str]], max_tokens=1024):
    # Estimate tokens (this is a simple heuristic, for exact calculation, use a tokenizer)
    total_tokens = 0
    messages = []
    while history_messages and total_tokens < max_tokens:
        message = history_messages.pop()
        messages.append({
            "role": message["role"],
            "content": message["content"]
        })
        
        tokens = len(message["content"].split())
        total_tokens += tokens
    
    return messages

    

def generate_ai_response(user_message: str, history_messages: List[Dict[str, str]]) -> str:
    # truncate the history messgaes
    messages = truncate_message_history(history_messages)
    messages.append({
        "role": "user",
        "content": user_message
    })
    
    print("generate_ai_response_messages: ", messages)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return completion.choices[0].message

def extract_json_from_ai_response(response: str) -> Dict:
    # Extract and transform JSON data from AI response
    print(response)
    json_start = '```json'
    json_end = '```'
    try:
        start = response.index(json_start)
        end = response.rindex(json_end)
        json_str = response[start+len(json_start):end]
        print(json_str)
        json_data = json.loads(json_str)
        return json_data
    except (ValueError, json.JSONDecodeError) as e:
        raise ValueError("Failed to extract JSON from AI response") from e