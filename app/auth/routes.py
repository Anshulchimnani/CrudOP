from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.auth.schema import LoginRequest
from app.database import get_db
from app.user.crud import get_user_by_email

router = APIRouter()

@router.post("/login")
def login_user(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, login_data.email)
    if not user or user.password != login_data.password:  # Plaintext for now
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": f"Welcome {user.name}!"}
