from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# controllers
from app.controllers.ai_controller import router as ai_router  # Adjust the import to your router module
from app.controllers.room_controller import router as room_router 

app = FastAPI()

# Define allowed origins
origins = [
    "http://localhost",
    "http://localhost:3000",
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ai_router, prefix="/ai")
app.include_router(room_router, prefix="/rooms")
