import sys
import os
import uvicorn

# Ensure the backend directory is in the python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
