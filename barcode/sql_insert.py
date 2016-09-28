from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sql_declarative import Base, Etiqueta, engine
from datetime import datetime

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

def dbinsert(cliente, barcode):
    nueva_etiqueta = Etiqueta(usuario='test', cliente=cliente, etiqueta_id=barcode,fecha=datetime.now(), hora = datetime.now())
    session.add(nueva_etiqueta)
    session.commit()
