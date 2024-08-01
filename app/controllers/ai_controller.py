from fastapi import APIRouter, HTTPException
import requests

# Models
from app.models.message import Message, NewMessage
from app.models.post import GeneratePostResponse

# Services
from app.services.ai_service import generate_ai_response, extract_json_from_ai_response
from app.services.room_service import save_message_to_room, get_room_messages

# utils
from datetime import datetime
from app.services.utils import generate_message_id

# constants
from app.constants.constant_ai_messages import TRANSFORM_PLAN_STRING_EDITOR_JS_JSON_MESSAGE

router = APIRouter()

@router.post("/messages/{roomId}", response_model=Message)
def add_message_to_room(roomId: str, new_message: NewMessage):
    # Create a user message
    user_message = Message(
        messageId=generate_message_id(),
        timestamp=new_message.timestamp,
        content=new_message.content,
        role="user"  # Ensure this complies with OpenAI roles
    )
    
    # Save user message to Firestore
    save_message_to_room(roomId, user_message)
    
    # Fetch all history messages in the room
    # Maybe not pass all the history messages to llm? - too expensive
    history_messages = get_room_messages(roomId)
    
    # Generate AI response using OpenAI API, passing all history messages
    ai_response = generate_ai_response(new_message.content, history_messages)
    ai_message = Message(
        messageId=generate_message_id(),
        timestamp=datetime.now().isoformat(),
        content=ai_response.content,
        role=ai_response.role  # Ensure this complies with OpenAI roles
    )
    
    # Save AI message to Firestore
    save_message_to_room(roomId, ai_message)
    
    return ai_message

@router.post("/messages/{roomId}/generate", response_model=GeneratePostResponse)
def generate_travel_json(roomId: str):
    # Fetch all history messages in the room
    history_messages = get_room_messages(roomId)
    
    # Generate AI response using OpenAI API, passing all history messages
    user_message = TRANSFORM_PLAN_STRING_EDITOR_JS_JSON_MESSAGE
    ai_response = generate_ai_response(user_message, history_messages)

    # Extract JSON data from AI response
    try:
        json_data = extract_json_from_ai_response(ai_response.content)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
     # Prepare the data for the Go backend service
    post_data = {
        "postTitle": "AI auto generate",
        "editorJsData": json_data
    }
    
    print("POST_DATA: ", post_data)

    # Call the Go backend service to create the post
    go_backend_url = "http://localhost:8081/travel/posts"  # Replace with your actual Go backend URL
    response = requests.post(go_backend_url, json=post_data)

    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail="Failed to create post in Go backend")
    
    return response.json()