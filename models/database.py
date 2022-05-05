from email.policy import default
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from decouple import config

DEBUG = config("DEBUG", default=False, cast=bool)


if DEBUG:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./my-fast-api.db"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    DATABASE_USER = config("DATABASE_USER")
    DATABASE_PASSWORD = config("DATABASE_PASSWORD ")
    DATABASE_NAME = config("DATABASE_NAME ")
    DATABASE_HOST = config("DATABASE_HOST ")
    SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"


seesion_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = seesion_local()
        yield db
    finally:
        db.close()
