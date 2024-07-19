# alpha/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

import uvicorn

app = FastAPI(title="AlphaBeta Chat API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins; adjust as needed for security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods; adjust as needed
    allow_headers=["*"],  # Allow all headers; adjust as needed
)

class Message(BaseModel):
    sender: str
    content: str

class ChatHistory(BaseModel):
    messages: List[Message] = []

chat_history = ChatHistory()

@app.get('/alive')
async def alive():
    return {'status': 'alive'}

@app.post("/chat")
async def chat(message: Message):
    chat_history.messages.append(message)
    # TODO: Implement AI response generation
    response = Message(
        sender="InventorSingh",
        content=f"Hello! I'm InventorSingh, the AI assistant for AlphaBeta. I received your message: {message.content}"
    )
    chat_history.messages.append(response)
    return response

@app.get("/history")
async def get_history():
    return chat_history

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
