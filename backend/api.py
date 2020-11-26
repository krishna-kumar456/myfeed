from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import main

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

@app.get("/keywords")
def read_root():
    return {"keywords": main.keywords}

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8081)