from sqlalchemy.orm import Session

from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

from models.users.users_model import UserBase, DbUser
from utils.hash import Hash


def create(db: Session, request: UserBase):
    new_user = DbUser(username=request.username, password=Hash.bcrypt(request.password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def read_users(db: Session):
    return db.query(DbUser).all()


def delete(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    db.delete(user)
    db.commit()
    return JSONResponse(content={"detail": f"User id {id} deleted"})


def read_user_by_id(db: Session, id: int):
    """
    select * from user where id = ?
    """
    return db.query(DbUser).filter(DbUser.id == id).first()


def update(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if user.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"user with {id} not found"
        )
    else:
        user.update(
            {
                DbUser.username: request.username,
                DbUser.password: Hash.bcrypt(request.password),
            }
        )
        db.commit()
        return JSONResponse(
            content={"detail": f"user id {id} updated successful"},
            status_code=status.HTTP_200_OK,
        )
