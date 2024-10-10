from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os
import json

import utility_v2

# Maintaining Directory & Reading necessary files

BASE_DIR = os.path.abspath(os.path.dirname("__file__"))
DATA_DIR = os.path.join(BASE_DIR, "data")

CREDS_PATH= os.path.join(DATA_DIR, 'creds.json')

with open(CREDS_PATH) as f:
    mysql_credentials = json.load(f)


# Initialize FastAPI app
app = FastAPI()


# Define a request model with a field 'message'

class MessageRequest(BaseModel):
    message: str


class UserRequest(BaseModel):
    employee_id: int


# Define a simple GET endpoint for the root URL

@app.get("/")
async def main():
    return {"message": "End-to-End Service Building"}


# Define an endpoint to handle POST requests

@app.post("/echo/")
async def echo_message(request: MessageRequest):
    # Pass the request message to the function and get the response
    processed_data = utility_v2.process_message(request.message)

    response = {
        "output": processed_data
    }

    return response

@app.post("/get-user/")
async def echo_message(request: UserRequest):

    user_id = request.employee_id

    # Connect to databases
    cnx = utility_v2.connect_mysql(CREDS_PATH)

    employee = utility_v2.return_user(cnx, user_id)

    response = {
        "output": employee
    }

    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5002)
