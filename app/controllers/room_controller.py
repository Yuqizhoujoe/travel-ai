from fastapi import APIRouter, HTTPException
from app.models.room import Room, NewRoom, NewRoomResponse, GetRoomResponse
from app.services.room_service import create_room, get_room
from app.exceptions import RoomNotFoundException

router = APIRouter()

@router.post("/", response_model=NewRoomResponse)
def create_room_controller(newRoom: NewRoom):
    try:
        roomId = create_room(newRoom.roomTitle)
        roomResponse = NewRoomResponse(roomId=roomId)
        return roomResponse
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{room_id}", response_model=GetRoomResponse)
def get_room_controller(room_id: str):
    try:
        room = get_room(room_id)
        return room
    except RoomNotFoundException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
