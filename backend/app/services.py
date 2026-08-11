import google.generativeai as genai
from app.config import settings
from app.schemas import MessageItem
from typing import List


class GeminiChatService:
    def __init__(self):
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(settings.DEFAULT_MODEL)

    def generate_chat_response(self, message: str, history: List[MessageItem]) -> str:
        formatted_history = []
        if history:
            for msg in history:
                role = "user" if msg.role == "user" else "model"
                formatted_history.append({
                    "role": role,
                    "parts": [msg.content]
                })

        chat = self.model.start_chat(history=formatted_history)
        response = chat.send_message(message)
        return response.text


chat_service = GeminiChatService()
