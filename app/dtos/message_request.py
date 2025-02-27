from pydantic import BaseModel

class MessageRequest(BaseModel):
    username: str
    system_message: str
    prompt: str