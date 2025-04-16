from fastapi import FastAPI
from app.base import Base
from app.database import engine
from app import user_api

app = FastAPI(title="CRED Operation API")

# Create tables at startup
Base.metadata.create_all(bind=engine)

app.include_router(user_api.router, prefix="/users", tags=["Users"])
