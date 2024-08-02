from pydantic import BaseModel
from typing import List

from app.models.message import Message

class Room(BaseModel):
    roomId: str
    roomTitle: str
    messages: List[Message] = []
    
class NewRoom(BaseModel):
    roomTitle: str
    
class NewRoomResponse(BaseModel):
    roomId: str
    
class GetRoomResponse(BaseModel):
    roomId: str
    roomTitle: str
    messages: List[Message] = []
