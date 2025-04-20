from fastapi import APIRouter
from fastapi.params import Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.user import crud, schema

router = APIRouter()
# Create a new user
@router.post("/", response_model=schema.UserRead)
def create_user(user_data: schema.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user_data)

# Get all users
@router.get("/", response_model=list[schema.UserRead])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db=db, skip=skip, limit=limit)

# Get user by ID
@router.get("/{user_id}", response_model=schema.UserRead)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_by_id(db=db, user_id=user_id)

# Update user by ID
@router.put("/{user_id}", response_model=schema.UserRead)
def update_user(user_id: int, user_data: schema.UserCreate, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user_id=user_id, user_data=user_data)

# Delete user by ID
@router.delete("/{user_id}", response_model=schema.UserRead)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db=db, user_id=user_id)
