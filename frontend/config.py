import os

# Backend API Endpoint URL
BACKEND_HOST = os.getenv("BACKEND_HOST", "127.0.0.1")
BACKEND_PORT = os.getenv("BACKEND_PORT", "8000")
DEFAULT_BACKEND_URL = f"http://{BACKEND_HOST}:{BACKEND_PORT}"

BACKEND_URL = os.getenv("BACKEND_URL", DEFAULT_BACKEND_URL)
CHAT_ENDPOINT = f"{BACKEND_URL}/chat"

# UI Page Config Settings
PAGE_TITLE = "Chat With Me"
PAGE_ICON = "💬"
