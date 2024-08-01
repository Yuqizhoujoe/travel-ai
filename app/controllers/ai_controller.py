from fastapi import APIRouter, HTTPException

# Models
from app.models.message import Message, NewMessage

# Services
from app.services.ai_service import generate_ai_response
from app.services.room_service import save_message_to_room, get_room_messages

# utils
from datetime import datetime
from app.services.utils import generate_message_id

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
