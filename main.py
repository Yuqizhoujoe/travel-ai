import uvicorn
from dotenv import load_dotenv
from app import app  # Ensure this correctly imports the app

# Load the .env file
load_dotenv()

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8082, reload=True, log_level="debug")
