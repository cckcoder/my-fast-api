from sqlalchemy.orm import Session

from fastapi.responses import JSONResponse

from models.users.users_model import UserBase, UserDisplayBase, DbUser


def create(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        password=request.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def read_users(db: Session):
    return db.query(DbUser).all()

"""
def delete(db: Session, id: int):
    inventory = db.query(DbInventory).filter(DbInventory.id == id).first()
    db.delete(inventory)
    db.commit()
    return JSONResponse(content={"detail": f"Inventory id {id} deleted"})




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
"""