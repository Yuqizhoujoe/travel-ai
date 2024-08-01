import os
from google.cloud import firestore
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Firestore DB
cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if not cred_path:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS environment variable is not set")

db = firestore.Client.from_service_account_json(cred_path)
