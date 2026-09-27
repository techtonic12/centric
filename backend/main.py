from fastapi import FastAPI

app = FastAPI(title="Centric")

@app.get("/")
def home():
    return{"message": "Centric backend is working!"}