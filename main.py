from fastapi import FastAPI

from routers.inventory import inventory_router
from routers.users import users_router

app = FastAPI()
app.include_router(inventory_router.router)
app.include_router(users_router.router)


@app.get("/")
def hello():
    return { "Hello": "FastAPI" }