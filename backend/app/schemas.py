from pydantic import BaseModel, Field
from typing import List, Optional


class MessageItem(BaseModel):
    role: str = Field(..., description="Role of the sender ('user' or 'assistant'/'model')")
    content: str = Field(..., description="Content of the message")


class ChatRequest(BaseModel):
    message: str = Field(..., description="The user's latest query message")
    history: Optional[List[MessageItem]] = Field(default=[], description="Previous message history")


class ChatResponse(BaseModel):
    response: Optional[str] = Field(None, description="The chatbot generated response")
    error: Optional[str] = Field(None, description="Error message if any occurred")
