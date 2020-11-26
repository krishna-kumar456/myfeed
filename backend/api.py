import uvicorn
import main

from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/best-hn")
def read_root():
    return {"response": main.get_hn_stories_json()}

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8081)