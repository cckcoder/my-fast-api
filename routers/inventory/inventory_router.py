from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(
    prefix="/inventory",
    tags=["inventory"]
)


class InventoryBase(BaseModel):
    description: str
    price: float
    stock: int


fake_inventory = [
    {"description": "pencil", "price": 15, "stock": 15},
    {"description": "laptop", "price": 5, "stock": 20},
    {"description": "books", "price": 25, "stock": 30},
]


@router.get("/")
def get_all_inventory(version: int = 1):
    if version > 1:
        return {"msg": "data not available"}
    else:
        return fake_inventory


@router.get("/{id}")
def inventory_by_id(id: int):
    item = fake_inventory[id - 1]
    return item


@router.post("/")
def post_api(inventory: InventoryBase):
    fake_inventory.append(inventory)
    return inventory


@router.put("/{id}")
def put_api(id: int, inventory: InventoryBase):
    fake_inventory[id - 1].update(**inventory.dict())
    item = fake_inventory[id - 1]
    return item


@router.delete("/{id}")
def delete_api(id: int):
    item = fake_inventory.pop(id - 1)
    return item