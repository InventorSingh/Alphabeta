from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Configure CORS
origins = [
    "*",
    "http://localhost",  # Allow your local development server
    "http://localhost:8000",  # Allow your API server
    "http://your-frontend-domain.com",  # Allow your frontend domain
    # Add any other origins you need
]

# Configure CORS to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

@app.get('/chat')
async def chat(message: str):
    return f"Hello {message}"


# Edit this to add the chain you want to add
# add_routes(app, NotImplemented)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
