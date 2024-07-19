#!/bin/bash

# Activate the virtual environment
source .myenv/bin/activate

# Run the uvicorn server
cd alpha

uvicorn main:app --reload --port 8000
