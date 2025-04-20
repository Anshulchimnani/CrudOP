from pydantic import BaseModel


class ProductCreate(BaseModel):
    id: str
    name: str
    description: str
    price: float
    stock: int


class ProductUpdate(BaseModel):
    name: str
    price: float
    stock: int

class ProductRead(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        from_attributes = True  # ✅ replaces orm_mode in Pydantic v2
