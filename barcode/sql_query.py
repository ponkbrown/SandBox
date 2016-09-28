from sql_declarative import Base, Etiqueta, engine
from sqlalchemy import create_engine
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
