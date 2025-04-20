from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.orders.schema import OrdersCreate
from app.orders.model import Orders



def create_order(db: Session, order: OrdersCreate):
    db_order = Orders(name=order.name, price=order.price)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Orders).offset(skip).limit(limit).all()

def update_orders(db: Session, order_id: int, order_data: OrdersCreate):
    orders = db.query(Orders).filter(Orders.id==order_id).first()
    if not orders:
        raise HTTPException(status_code=404, detail="User not found")

    orders.name = order_data.name

    db.commit()
    db.refresh(orders)
    return orders

