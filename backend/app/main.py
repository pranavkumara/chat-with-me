from fastapi import FastAPI, HTTPException
from app.config import settings
from app.schemas import ChatRequest, ChatResponse
from app.services import chat_service

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="FastAPI Backend for Gemini Chatbot"
)


@app.get("/")
def root():
    return {
        "status": "online",
        "message": f"{settings.PROJECT_NAME} is running",
        "version": settings.VERSION
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        reply = chat_service.generate_chat_response(
            message=request.message,
            history=request.history or []
        )
        return ChatResponse(response=reply)
    except Exception as e:
        return ChatResponse(error=str(e))
