from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/alive")
async def alive():
    return {"status": "alive"}

@app.post("/chat")
async def chat(message: str):
    # Here we will call an AI model like ChatGPT, ClaudAI, Ollama(my fav!)
    # Ollama is easy to integrate with Python! No API Key required!
    # For now, we'll just echo the message back
    return {"response": f"You said: {message}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)