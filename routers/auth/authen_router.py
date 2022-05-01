from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm.session import Session
from models.database import get_db
from models.users.users_model import DbUser

from utils.hash import Hash
from utils.oauth2 import create_access_token



router = APIRouter(tags=["authentication"])


@router.post("/token")
def login():
    return {"hello": "token"}
