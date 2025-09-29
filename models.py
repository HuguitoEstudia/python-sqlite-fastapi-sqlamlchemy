from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

app = FastAPI()

DATABASE_URL = "sqlite:///./dev.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})

Base = declarative_base()


class Persona(Base):
    __tablename__ = "personas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    edad = Column(Integer)
    dni = Column(Integer)

Base.metadata.create_all(engine)