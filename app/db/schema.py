from signal import strsignal
from pydantic import BaseModel


class StockRequest(BaseModel):
    symbol: str

class StockResponse(BaseModel):
    id: int
    symbol: str
    price: float
    forward_pe: float
    forward_eps: float     
    dividend_yield: float
    ma50: float
    ma200: float
    