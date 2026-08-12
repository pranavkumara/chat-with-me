import subprocess
import sys
import os
import time
import urllib.request

def wait_for_backend(url: str, timeout: int = 15):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with urllib.request.urlopen(url, timeout=2) as resp:
                if resp.status == 200:
                    return True
        except Exception:
            pass
        time.sleep(0.5)
    return False

def main():
    print("=" * 60)
    print("🚀 Starting Gemini Chatbot Application Services...")
    print("=" * 60)

    backend_host = os.getenv("BACKEND_HOST", "127.0.0.1")
    backend_port = os.getenv("BACKEND_PORT", "8000")
    frontend_port = os.getenv("PORT", "8501")

    # 1. Start FastAPI Backend
    print(f"🔹 Launching FastAPI Backend (http://{backend_host}:{backend_port})...")
    backend_proc = subprocess.Popen(
        [sys.executable, os.path.join("backend", "run.py")],
        cwd=os.path.dirname(os.path.abspath(__file__))
    )

    # Wait for backend to be responsive
    health_url = f"http://{backend_host}:{backend_port}/"
    print(f"⏳ Waiting for backend health check at {health_url}...")
    if wait_for_backend(health_url, timeout=15):
        print("✅ Backend ready!")
    else:
        print("⚠️ Backend took longer than expected to start; proceeding with frontend startup.")

    # 2. Start Streamlit Frontend
    print(f"🔹 Launching Streamlit Frontend on 0.0.0.0:{frontend_port}...")
    frontend_proc = subprocess.Popen(
        [
            sys.executable, "-m", "streamlit", "run",
            os.path.join("frontend", "app.py"),
            "--server.port", str(frontend_port),
            "--server.address", "0.0.0.0",
            "--server.headless", "true"
        ],
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
