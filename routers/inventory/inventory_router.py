from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.inventory.inventory_model import InventoryBase

from routers.inventory import inventory_controller

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"]
)


@router.get("/")
def get_all_inventory(version: int = 1):
    pass

@router.get("/{id}")
def inventory_by_id(id: int):
    pass


@router.post("/")
def create_inventory(request: InventoryBase, db: Session = Depends(get_db)):
    return inventory_controller.create(db, request)


@router.put("/{id}")
def put_api(id: int, inventory: InventoryBase):
    pass


@router.delete("/{id}")
def delete_api(id: int):
    pass