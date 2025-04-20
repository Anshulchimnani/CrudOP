from app.base import Base
from app.database import engine
from app.orders.model import Orders

# Create all tables
Base.metadata.create_all(bind=engine)
