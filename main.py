from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pypdf import PdfReader

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your CV
def load_cv():
    reader = PdfReader("cv.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

cv_text = load_cv()

@app.get("/")
def home():
    return {"message": "Backend is working"}

# Chatbot endpoint
@app.get("/chat")
def chat(q: str):
    q = q.lower()

    if "skill" in q:
        return {"answer": "I am skilled in Python, AI, Data Analysis, and Research."}

    if "project" in q:
        return {"answer": "I have worked on AI for breast cancer and cervical cancer."}

    if "hire" in q:
        return {"answer": "You can contact me via WhatsApp, Email, or Call."}

    return {"answer": "I am an AI developer and research assistant. Ask me anything!"}

# CV endpoint
@app.get("/cv")
def get_cv():
    return {"cv": cv_text}