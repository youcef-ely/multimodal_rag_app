
import sys
from fastapi import FastAPI
from pydantic import BaseModel
from backend.worker import request_response

class UserInput(BaseModel):
    query: str

app = FastAPI()

@app.post("/generate")
def generate(input: UserInput):
    response = request_response(input.query)
    return response
