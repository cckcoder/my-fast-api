from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.users.users_model import UserBase, UserDisplayBase

from models.users.users_model import UserBase
from routers.users import users_controller


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def get_all_user(db: Session = Depends(get_db)):
    return users_controller.read_users(db)


@router.post("/")
def register_user(request: UserBase, db: Session = Depends(get_db)):
    return users_controller.create(db, request)
