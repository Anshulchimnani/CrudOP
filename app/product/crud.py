from sqlalchemy.orm import Session
from app.product.model import Product
from app.product.schema import ProductCreate, ProductUpdate



def create_product(db: Session, product:ProductCreate):
    db_product = Product(name=product.name, description=product.description, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db: Session, product_id: int, product_data: ProductUpdate):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        if product_data.name:
            db_product.name = product_data.name
        if product_data.description:
            db_product.description = product_data.description
        if product_data.price:
            db_product.price = product_data.price
        if product_data.stock is not None:
            db_product.stock = product_data.stock
        db.commit()
        db.refresh(db_product)
    return db_product

# Delete product
def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
