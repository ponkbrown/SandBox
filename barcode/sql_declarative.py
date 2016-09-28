from sqlalchemy import (create_engine, Column, Date, DateTime, Integer, String, Table)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Etiqueta(Base):
    __tablename__ = 'etiqueta'
    # Definimos las columnas para la etiqueta
    id = Column(Integer, primary_key=True)
    usuario = Column(String(50))
    cliente = Column(String(50))
    etiqueta_id = Column(String(50))
    fecha = Column(Date)
    hora = Column(DateTime)

# Creamos el motor para la base de datos en directorio local
engine = create_engine('sqlite:///etiquetas.db', echo=False)

# Crea las tablas
Base.metadata.create_all(engine)
