from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: int
    message: int
    price: float
    is_offer: Optional[bool] = None

@app.get("/name/{item_id}/message/{message_id}")
def read_name(item_id: int,message_id: int, q:Optional[str] = None,message: Optional[str] = None):
    return f"Hello {q}! {message}"