from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def main():
    return {
        "name": "Huzaifa",
        "email": "abc@gmail.com",
        "body": "Hello world all!"
}

@app.post("/users")
def PostData(name, email, body):
    return {
        "message": "Data received successfully!"
    }