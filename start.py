import subprocess
import sys
import os
import time

def main():
    print("=" * 60)
    print("🚀 Starting Gemini Chatbot Application Services...")
    print("=" * 60)

    # 1. Start FastAPI Backend
    print("🔹 Launching FastAPI Backend (http://127.0.0.1:8000)...")
    backend_proc = subprocess.Popen(
        [sys.executable, os.path.join("backend", "run.py")],
        cwd=os.path.dirname(os.path.abspath(__file__))
    )

    # Give backend a moment to initialize
    time.sleep(2)

    # 2. Start Streamlit Frontend
    print("🔹 Launching Streamlit Frontend...")
    frontend_proc = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", os.path.join("frontend", "app.py")],
        cwd=os.path.dirname(os.path.abspath(__file__))
    )

    print("\n✅ Both services started successfully!")
    print("   Press CTRL+C in this terminal to stop all services.\n")

    try:
        backend_proc.wait()
        frontend_proc.wait()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down services...")
        backend_proc.terminate()
        frontend_proc.terminate()
        backend_proc.wait()
        frontend_proc.wait()
        print("👋 Services stopped cleanly.")

if __name__ == "__main__":
    main()
