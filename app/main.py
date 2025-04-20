from fastapi import FastAPI
from app.user.routes import router as user_router
from app.product.routes import router as product_router
from app.orders.routes import router as orders_router
from app.auth.routes import router as auth_router
from app.database import engine
from app.user import model as user_model
from app.product import model as product_models
from app.orders import model as orders_model

# Make sure all models are imported before creating tables
user_model.Base.metadata.create_all(bind=engine)
product_models.Base.metadata.create_all(bind=engine)
orders_model.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Controller API Services")

@app.get("/")
def read_root():
    return {"status": "API is running"}


#include routers
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(product_router, prefix="/products", tags=["Products"])
app.include_router(orders_router, prefix="/orders", tags=["Orders"])
app.include_router(auth_router, prefix="/auth", tags=["Auths"])
