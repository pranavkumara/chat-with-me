import os

# Backend API Endpoint URL
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
CHAT_ENDPOINT = f"{BACKEND_URL}/chat"

# UI Page Config Settings
PAGE_TITLE = "Chat With Me"
PAGE_ICON = "💬"
