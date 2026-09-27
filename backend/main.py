from fastapi import FastAPI
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Centric")

@app.get("/")
def home():
    return{"message": "Centric backend is working!"}