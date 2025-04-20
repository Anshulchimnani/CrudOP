from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.product import crud, schema
from app.database import get_db
from app.product.schema import ProductUpdate, ProductCreate, ProductRead

router = APIRouter()

@router.post("/", response_model=schema.ProductRead)
def create_product(product_data: schema.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product=product_data)

@router.get("/", response_model=list[schema.ProductRead])
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_product(db=db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schema.ProductRead)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    return crud.get_product_by_id(db, product_id=product_id)

@router.put("/{id}", response_model=schema.ProductRead)
def update_product(product_id: int, product_data: ProductUpdate, db: Session = Depends(get_db)):
    return crud.update_product(db, product_id=product_id, product_data=product_data)

@router.delete("/{id}", response_model=schema.ProductRead)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db, product_id=product_id)