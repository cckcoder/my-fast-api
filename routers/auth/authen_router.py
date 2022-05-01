from fastapi import APIRouter, Depends, status, HTTPException


router = APIRouter(
    tags=["authentication"]
)


@router.post("/token")
def login():
    return { "hello": "token" }