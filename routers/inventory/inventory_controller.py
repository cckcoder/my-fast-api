from sqlalchemy.orm import Session

from fastapi.responses import JSONResponse

from models.inventory.inventory_model import DbInventory, InventoryBase


def create(db: Session, request: InventoryBase):
    new_inventory = DbInventory(
        description=request.description, price=request.price, stock=request.stock
    )

    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    return new_inventory


def delete(db: Session, id: int):
    inventory = db.query(DbInventory).filter(DbInventory.id == id).first()
    db.delete(inventory)
    db.commit()
    return JSONResponse(content={"detail": f"Inventory id {id} deleted"})


def read_inventory(db: Session):
    return db.query(DbInventory).all()


def read_inventory_by_id(db: Session, id: int):
    return db.query(DbInventory).filter(DbInventory.id == id).first()


def update(db: Session, id: int, request: InventoryBase):
    inventory = db.query(DbInventory).filter(DbInventory.id == id).first()
    inventory.description = request.description
    inventory.price = request.price
    inventory.stock = request.stock
    db.commit()
    db.refresh(inventory)
    return inventory
