from fastapi import BackgroundTasks, Depends, FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy import null
from sqlalchemy.orm import Session
import uvicorn
from pathlib import Path
import yfinance as yf

from app.db import models
from app.db.schema import StockRequest
from app.db.database import SessionLocal, get_db, engine

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
def fetch_stock_data(id: int):
    db = SessionLocal()
    stock = db.query(models.Stock).filter(models.Stock.id == id).first()
    
    yahoo_data = yf.Ticker(stock.symbol)

    stock.ma200 = yahoo_data.info['twoHundredDayAverage']
    stock.ma50 = yahoo_data.info['fiftyDayAverage']
    stock.price = yahoo_data.info['previousClose']
    stock.forward_pe = yahoo_data.info['forwardPE']
    stock.forward_eps = yahoo_data.info['forwardEps']

    if yahoo_data.info['dividendYield'] is not None:
        stock.dividend_yield = yahoo_data.info['dividendYield'] * 100


    db.add(stock)
    db.commit()

@app.post("/stock")
async def create_stock(stockrequest: StockRequest, backgroundtasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Creates a stock and stores it in the database
    """
    stock = models.Stock()
    stock.symbol = stockrequest.symbol
    db.add(stock)
    db.commit()

    backgroundtasks.add_task(fetch_stock_data, stock.id)

    return {
        "code": "success",
        "message": "stock created"
    }

