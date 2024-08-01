from pydantic import BaseModel 
from typing import Optional, Literal

class Message(BaseModel):
    messageId: Optional[str] = None
    timestamp: str
    content: str
    role: Literal["user", "assistant", "system"]

class NewMessage(BaseModel):
    content: str
    timestamp: str
