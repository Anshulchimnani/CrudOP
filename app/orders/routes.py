from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.orders import crud, schema
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schema.OrdersRead)
def create_orders(orders_data: schema.OrdersCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order=orders_data)

@router.get("/", response_model=list[schema.OrdersRead])
def get_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_orders(db=db, skip=skip, limit=limit)
