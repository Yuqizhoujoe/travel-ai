# firebase
from google.cloud import firestore
from app.services.firebase import db

# Models
from app.models.message import Message

def save_message_to_room(room_id: str, message: Message):
    room_ref = db.collection('rooms').document(room_id)
    room = room_ref.get()
    
    message_data = {
        'messageId': message.messageId,
        'timestamp': message.timestamp,
        'role': message.role,
        'content': message.content
    }
    
    if room.exists:
        room_data = room.to_dict()
        messages = room_data.get('messages', [])
        
        # Check for duplication
        if any(m['messageId'] == message.messageId for m in messages):
            print("Message already exists, skipping insertion.")
            return

        room_ref.update({
            'messages': firestore.ArrayUnion([message_data])
        })
    else:
        room_ref.set({
            'room_id': room_id,
            'room_title': 'Hardcoded Room Title',  # Replace this with dynamic data as needed
            'messages': [message_data]
        })

def get_room_messages(room_id: str) -> list:
    room_ref = db.collection('rooms').document(room_id)
    room = room_ref.get()
    
    if room.exists:
        room_data = room.to_dict()
        return room_data.get('messages', [])
    else:
        return []
