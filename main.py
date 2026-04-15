from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pypdf import PdfReader

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_cv():
    try:
        reader = PdfReader("cv.pdf")
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except:
        return "CV not available"

try:
    cv_text = load_cv()
except:
    cv_text = "CV not available"

@app.get("/")
def home():
    return {"message": "Backend is working"}

@app.get("/chat")
def chat(q: str):
    q = q.lower()

    if "skill" in q:
        return {"answer": "I am skilled in Python, AI, Data Analysis, and Research."}

    if "project" in q:
        return {"answer": "I have worked on AI for breast cancer and cervical cancer."}

    return {"answer": "Ask me about my skills, projects or hiring."}

@app.get("/cv")
def get_cv():
    return {"cv": cv_text}
