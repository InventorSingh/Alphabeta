from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

from pydantic import BaseModel

class Message(BaseModel):
    sender: str
    content: str

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

@app.post('/chat')
async def chat(message: Message):
    new_message = Message(sender="Server", content=f"Received your message: {message.content}")
    return new_message

# Serve the HTML file from the root
@app.get("/home")
async def read_root():
    return FileResponse("static/index.html")

# Edit this to add the chain you want to add
# add_routes(app, NotImplemented)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
