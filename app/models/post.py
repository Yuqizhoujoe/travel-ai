from pydantic import BaseModel
# from typing

class GeneratePostResponse(BaseModel):
    postId: str
    success: bool