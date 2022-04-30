from decimal import Decimal
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, DECIMAL
from sqlalchemy.sql import func

from decimal import Decimal
from models.database import Base
from pydantic import BaseModel


class DbInventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    descrition = Column(String)
    price = Column(DECIMAL)
    stock = Column(Integer)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(
        DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now()
    )



class InventoryBase(BaseModel):
    description: str
    price: Decimal
    stock: int