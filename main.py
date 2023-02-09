from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn

from enum import Enum
from typing import Union
from pydantic import BaseModel

from sqlalchemy.orm import Session

from sql_app import models
from sql_app.database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


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

if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=8005, reload=True)
