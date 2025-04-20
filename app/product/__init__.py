from app.base import Base
from app.database import engine
from app.product.model import Product  # Make sure all models are imported so Base knows about them

# Create all tables
Base.metadata.create_all(bind=engine)
