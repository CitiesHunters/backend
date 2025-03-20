from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def create_database():
    """
    Inizializza il database creando tutte le tabelle definite nei modelli
    che ereditano da 'Base'. DA NON USARE IN PRODUZIONE.
    """
    Base.metadata.create_all(bind=engine)


def get_db():
    """
    Fornisce una sessione del database da utilizzare nelle operazioni CRUD.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()