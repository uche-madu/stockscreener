from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import uvicorn
from pathlib import Path

from app.db import models
from app.db.database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'app/templates')))

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    """
    Displays the stock screener dashboard / homepage
    """
    return templates.TemplateResponse("dashboard.html", 
        {
        "request": request
        }
    )

@app.post("/stock")
def create_stock():
    """
    Creates a stock and stores it in the database
    """
    return {
        "code": "success",
        "message": "stock created"
    }

#if __name__ == "__main__":
#    uvicorn.run("main:app", host='localhost', port=8005, reload=True)
