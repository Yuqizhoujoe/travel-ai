from fastapi import APIRouter, HTTPException

# Models
from app.models.room import Room, NewRoom, NewRoomResponse

# Services
from app.services.room_service import create_room

router = APIRouter()

@router.post("/", response_model=NewRoomResponse)
def create_room_controller(newRoom: NewRoom):
    try:
        roomId = create_room(newRoom.roomTitle)
        roomResponse = NewRoomResponse(roomId=roomId)
        return roomResponse
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))