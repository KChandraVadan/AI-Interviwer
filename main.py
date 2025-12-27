from fastapi import FastAPI, UploadFile
from stt import transcribe_audio
from ocr import extract_text_from_image
from analyzer import analyze_content
from interviewer import generate_questions
from scoring import score_student

app = FastAPI()

context_store = {
    "content": "",
    "responses": []
}

@app.post("/transcribe")
async def transcribe(audio: UploadFile):
    text = transcribe_audio(audio.file)
    context_store["responses"].append(text)
    return {"transcript": text}

@app.post("/ocr")
async def ocr(image: UploadFile):
    text = extract_text_from_image(image.file)
    context_store["content"] += text
    return {"screen_text": text}

@app.get("/question")
def get_question():
    question = generate_questions(context_store)
    return {"question": question}

@app.get("/final-score")
def final_score():
    return score_student(context_store)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "AI-Based Project Interview System"
    }

