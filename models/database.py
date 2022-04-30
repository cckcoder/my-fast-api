from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./my-fast-api.db"


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thred": False})

seesion_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = seesion_local()
        yield db
    finally:
        db.close()
