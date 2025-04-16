from sqlalchemy.orm import Session
from app.database import get_db
from app import user_crud
from app.user_schema import UserCreate, UserRead
from fastapi import APIRouter, Depends, HTTPException



router = APIRouter()

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user)

@router.get("/", response_model=list[UserRead])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user_crud.get_users(db, skip=skip, limit=limit)

@router.put("/{id}", response_model=UserRead)
def update_user(id: int, user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.update_user(db, id, user)