from pydantic import BaseModel, EmailStr
from typing import Optional, List
from app.orders.schema import OrdersRead

#Input for creating a user
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

#This is the DTO response to user
class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    orders: Optional[List[OrdersRead]] = []

    class Config:
        from_attributes = True  # ✅ replaces orm_mode in Pydantic v2

#This is the updates
class UserUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None