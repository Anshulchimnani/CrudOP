from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Orders(Base):
    __tablename__ = "Orders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

