from sqlalchemy.orm import Session

from fastapi.responses import JSONResponse

from models.inventory.inventory_model import DbInventory, InventoryBase


def create(db: Session, request: InventoryBase):
    new_inventory = DbInventory(
        description=request.description,
        price=request.price,
        stock=request.stock
    )
    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    return new_inventory


def read_inventory(db: Session):
    return db.query(DbInventory).all()