from models import Persona,engine,app
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Boolean

Session = sessionmaker(bind=engine)

session = Session()

# persona = Persona(nombre="pepe",apellido="pepon",edad=30,dni=1234567)

# session.add(persona)

# session.commit()

@app.post("/create_persona/",tags=["Personas"],)
def create_persona(nombre:str,
                   apellido:str,
                   edad:int=0,
                   dni:int=1234567):
    
    persona = Persona(nombre=nombre,
                      apellido=apellido,
                      edad=edad,
                      dni=dni)
    
    session.add(persona)
    session.commit()
    session.refresh(persona)

@app.get("/get_all_personas/",tags=["Personas"])
def get_all_personas():
    return session.query(Persona).all()

@app.get("/get_persona_by_id/{item_id}",tags=["Personas"])
def get_persona_by_id(item_id:int = 0):
    return session.get(Persona,item_id)