# AlphaBeta Chat Application: Getting Started Guide

Hello! Welcome to the AlphaBeta project. This guide will help you set up and run both the frontend and backend of our chat application. Let's get started!

## What You'll Need

- Python 3.7 or newer
- A text editor (like VS Code, Sublime Text, or even Notepad)
- A command line interface (Terminal on Mac/Linux, Command Prompt or PowerShell on Windows)

## Project Structure

First, let's set up our project structure:

```
AlphaBeta-chat/
│
├── frontend/
│   └── index.html
│
└── backend/
    └── main.py
```

## Step 1: Setting Up the Frontend

1. Create a folder named `AlphaBeta-chat` on your computer.
2. Inside `AlphaBeta-chat`, create another folder named `frontend`.
3. In the `frontend` folder, create a file named `index.html`.
4. Copy the HTML content provided earlier into this `index.html` file.

## Step 2: Running the Frontend

1. Open your command line interface.
2. Navigate to the `frontend` folder. You can do this by typing:
   ```
   cd path/to/AlphaBeta-chat/frontend
   ```
3. Start a simple Python web server by running:
   ```
   python -m http.server 8000
   ```
4. Open a web browser and go to `http://localhost:8000`. You should see the AlphaBeta chat interface!

## Step 3: Setting Up the Backend

1. In the `AlphaBeta-chat` folder, create another folder named `backend`.
2. In the `backend` folder, create a file named `main.py`.
3. Open `main.py` in your text editor and add the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/alive")
async def check_alive():
    return {"status": "alive"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

4. Install the required packages. In your command line, run:
   ```
   pip install fastapi uvicorn
   ```

## Step 4: Running the Backend

1. Open a new command line window (keep the frontend server running in the other one).
2. Navigate to the `backend` folder:
   ```
   cd path/to/AlphaBeta-chat/backend
   ```
3. Start the FastAPI server by running:
   ```
   python main.py
   ```
4. The server should start, and you'll see some output indicating it's running.

## Step 5: Testing the Backend

1. Open a web browser and go to `http://localhost:8000/alive`.
2. You should see a JSON response: `{"status": "alive"}`.
3. Congratulations! Your backend is up and running.

## What's Next?

Now that you have both the frontend and backend running:

1. The frontend is served at `http://localhost:8000` (using the Python simple server).
2. The backend API is available at `http://localhost:8000` (using FastAPI).

Note: In a real-world scenario, we'd use different ports for frontend and backend, but this setup works for now.

To continue developing:

1. Modify the `index.html` file to change the frontend appearance or behavior.
2. Add more endpoints to `main.py` to create new API functionalities.
3. Implement the chat functionality by connecting the frontend to the backend API.

Remember to refresh your browser after making changes to the frontend, and restart the backend server after modifying `main.py`.

Happy coding! If you have any questions, don't hesitate to ask.