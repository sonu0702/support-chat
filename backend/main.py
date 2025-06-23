from typing import Annotated, Union
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

from agents.support_chat import Support_chat

app = FastAPI()


@app.get("/health")
def health():
    return {"health":"ok"}

class QuestionRequest(BaseModel):
    question: str

class QuestionResponse(BaseModel):
    answer: str

@app.post("/ask", response_model=QuestionResponse)
async def ask_question(request : QuestionRequest):
    if not request.question or not request.question.strip():
        raise HTTPException(status_code=503,detail='Question cannot be empty.')
    
    try:
        support = Support_chat()
        answer = support.ask(question=request.question)
        return QuestionResponse(answer=answer)
    except Exception as e:
        print(f"Error in /ask endpoint for question '{request.question}': {e}")
        raise HTTPException(status_code=500, detail="An internal error occurred.")
