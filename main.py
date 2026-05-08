from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

app = FastAPI()


# -----------------------------
# Request Models
# -----------------------------

class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


# -----------------------------
# Home Endpoint
# -----------------------------

@app.get("/")
def home():
    return {"message": "SHL AI Assistant Running"}


# -----------------------------
# Health Endpoint
# -----------------------------

@app.get("/health")
def health():
    return {"status": "ok"}


# -----------------------------
# Chat Endpoint
# -----------------------------

@app.post("/chat")
def chat(request: ChatRequest):

    latest_message = request.messages[-1].content.lower()

    recommendations = []

    if "java" in latest_message:
        recommendations = [
            "Java Coding Test",
            "Core Java Assessment",
            "Problem Solving Test"
        ]

    elif "python" in latest_message:
        recommendations = [
            "Python Coding Test",
            "Python Developer Assessment",
            "Analytical Skills Test"
        ]

    elif "frontend" in latest_message:
        recommendations = [
            "HTML/CSS Test",
            "JavaScript Assessment",
            "React Skills Test"
        ]

    else:
        recommendations = [
            "Cognitive Ability Test",
            "Technical Skills Assessment"
        ]

    return {
        "reply": "Recommended assessments based on your hiring requirements.",
        "recommendations": recommendations,
        "end_of_conversation": False
    }