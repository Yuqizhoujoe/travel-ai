from uuid import uuid4

def generate_message_id() -> str:
    return str(uuid4())
