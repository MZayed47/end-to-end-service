from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from utility_v1 import process_message

# Initialize FastAPI app
app = FastAPI()


# Define a request model with a field 'message'

class MessageRequest(BaseModel):
    message: str


# Define a simple GET endpoint for the root URL

@app.get("/")
async def main():
    return {"message": "End-to-End Service Building"}


# Define an endpoint to handle POST requests

@app.post("/echo/")
async def echo_message(request: MessageRequest):
    # Pass the request message to the function and get the response
    processed_data = process_message(request.message)

    response = {
        "output": processed_data
    }

    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)
