from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserRead(UserCreate):
    id: int

    class Config:
        from_attributes = True  # ✅ replaces orm_mode in Pydantic v2
