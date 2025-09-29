from models import Persona,engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()

persona = Persona(nombre="pepe",apellido="pepon",edad=30,dni=1234567)

session.add(persona)

session.commit()