from pydantic import BaseModel

class OrdersCreate(BaseModel):
    id: int
    name: str
    price: float
    stock: int

class OrdersRead(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        from_attributes = True  # ✅ replaces orm_mode in Pydantic v2
