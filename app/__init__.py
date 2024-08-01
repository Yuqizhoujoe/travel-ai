from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.ai_controller import router as ai_router  # Adjust the import to your router module

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
