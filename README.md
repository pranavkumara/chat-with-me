# 💬 Gemini Chatbot

A modular, full-stack Python application utilizing Google's **Gemini AI** model with a **FastAPI** backend server and a **Streamlit** interactive web dashboard.

---

## 📁 Project Structure

```
chatbot/
├── backend/                    # FastAPI Backend Application
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py           # App settings & Gemini API configuration
│   │   ├── schemas.py          # Pydantic request/response models
│   │   ├── services.py         # Gemini AI model interaction service
│   │   └── main.py             # FastAPI routes & application setup
│   └── run.py                  # Entrypoint runner for FastAPI server
├── frontend/                   # Streamlit Frontend Application
│   ├── app.py                  # Main Streamlit UI interface
│   └── config.py               # Frontend configuration (API URLs, UI settings)
├── .env                        # Local environment variables (Git-ignored)
├── .env.example                # Example environment file template
├── .gitignore                  # Git ignore configuration
├── README.md                   # Documentation and instructions
├── requirements.txt            # Project dependencies
└── start.py                    # Multi-process launcher script
```

---

## ⚡ Quick Start

### 1. Prerequisites & Virtual Environment Setup

Ensure you have Python installed. Activate your virtual environment if you haven't already:

```bash
# Activate existing virtualenv (Windows)
.\chatbot\Scripts\activate
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Environment Setup

Copy `.env.example` to `.env` and add your **Gemini API Key**:

```bash
# Windows PowerShell
Copy-Item .env.example .env
```

Open `.env` and set your key:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

---

## 🚀 Running the Application

### Option A: Launch Everything Simultaneously (Recommended)

Run the unified launcher script:
```bash
python start.py
```
This automatically starts both:
- **FastAPI Backend**: `http://127.0.0.1:8000`
- **Streamlit Frontend**: opens in your browser at `http://localhost:8501`

---

### Option B: Launch Backend and Frontend Separately

**Terminal 1 (Backend):**
```bash
python backend/run.py
```

**Terminal 2 (Frontend):**
```bash
streamlit run frontend/app.py
```

---

## 🌐 Render Deployment (Single Server)

To deploy both FastAPI backend and Streamlit frontend in a single Render Web Service:

1. **Create Web Service on Render**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python start.py`

2. **Environment Variables on Render**:
   - `GEMINI_API_KEY`: Your Gemini API Key
   - `BACKEND_PORT`: `8000` (internal port for FastAPI)
   - `BACKEND_HOST`: `127.0.0.1`

> **Note**: Render automatically injects a `PORT` environment variable which `start.py` assigns to Streamlit so external traffic reaches the Streamlit dashboard, while FastAPI runs internally on `BACKEND_PORT`.

