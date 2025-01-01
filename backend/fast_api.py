import os, sys
from fastapi import FastAPI
from pydantic import BaseModel

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..', 'backend'))

from worker import request_response


class UserInput(BaseModel):
    query: str

app = FastAPI()

@app.post("/generate")
def generate(input: UserInput):
    response = request_response(input.query)
    return response
