from sqlalchemy import Column, String, Date, TIMESTAMP, BIGINT
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import Session
from app.schemas.auth import UserRegistration

class User(Base):
    """
    Modello SQLAlchemy per la tabella 'users' che memorizza le informazioni degli utenti.
    Un primo abbozzo, sicuramente aggiungeremo altro immagino
    """

    __tablename__ = "users"

    user_id = Column(BIGINT, primary_key=True, index=True, autoincrement=True)
    phone_number = Column(String(20), unique=True, nullable=True, index=True)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(250), nullable=False)
    birth_date = Column(Date, nullable=True)
    custom_tag = Column(String(100), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())

    @staticmethod
    def create(user_model : UserRegistration, db : Session):
        """
        Metodo di classe per creare un nuovo utente nel database.
        """
        new_user = User(**user_model.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
