from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy.orm import Session
from models.database import get_db
from models.inventory.inventory_model import InventoryBase, InventoryDisplayBase

from routers.inventory import inventory_controller

router = APIRouter(prefix="/inventory", tags=["inventory"])


@router.get("/", response_model=List[InventoryDisplayBase])
def get_all_inventory(db: Session = Depends(get_db)):
    return inventory_controller.read_inventory(db)


@router.get("/{id}")
def inventory_by_id(id: int, db: Session = Depends(get_db)):
    return inventory_controller.read_inventory_by_id(db, id)


@router.post("/")
def create_inventory(request: InventoryBase, db: Session = Depends(get_db)):
    return inventory_controller.create(db, request)


@router.put("/{id}")
def put_api(id: int, request: InventoryBase, db: Session = Depends(get_db)):
    return inventory_controller.update(db, id, request)


@router.delete("/{id}")
def delete_api(id: int, db: Session = Depends(get_db)):
    return inventory_controller.delete(db, id)
