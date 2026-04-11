from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from google import genai

# 1. Load the secret key and connect to Gemini
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# 2. Start the FastAPI server
app = FastAPI(title="AI Cover Letter Generator")

# 3. Allow our future Frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Define what data we expect from the user (Frontend)
class CoverLetterRequest(BaseModel):
    resume: str
    job_description: str

# 5. The Core Engine: Where the AI does the work
@app.post("/generate")
def generate_cover_letter(data: CoverLetterRequest):
    
    # PROMPT ENGINEERING: This is how we control the AI's behavior.
    # We don't just pass the text; we give it strict professional rules.
    master_prompt = f"""
    You are an expert technical recruiter and professional copywriter.
    Your task is to write a highly tailored, professional, and confident cover letter.
    
    RULES:
    - Keep it under 350 words.
    - Do NOT be overly robotic or use cliché words like "I am writing to express my interest..."
    - Match the skills in the Resume to the requirements in the Job Description.
    - Start with a strong hook.
    
    Here is the candidate's Resume:
    {data.resume}
    
    Here is the Job Description they are applying for:
    {data.job_description}
    """
    
    print("Asking Gemini to write the letter...")
    
    # Send the master prompt to Gemini 2.5 Flash
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=master_prompt
    )
    
    # Send the finished letter back to the internet
    return {
        "status": "success",
        "cover_letter": response.text
    }

# Quick check to see if server is awake
@app.get("/")
def home():
    return {"message": "AI Cover Letter API is running!"}   