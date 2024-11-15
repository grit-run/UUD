import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SQLALCHEMY_DATABASE_URL = 'postgresql://{user}:{password}@{host}:{port}/{database}'.format(
    user=os.getenv("AL_USER"),
    password=os.getenv("AL_PASS"),
    host=os.getenv("AL_HOST"),
    port=os.getenv("AL_PORT"),
    database=os.getenv("AL_DB")
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def create_db():
    Base.metadata.create_all(bind=engine)
