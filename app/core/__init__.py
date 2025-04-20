from app.base import Base
from app.database import engine

# Create all tables
Base.metadata.create_all(bind=engine)
