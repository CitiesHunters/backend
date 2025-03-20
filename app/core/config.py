from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
load_dotenv()

class Settings(BaseSettings):
    """
    Classe di configurazione per l'applicazione. Probabilmente aggiungeremo o 
    cambieremo altre cose in futuro.
    """
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 300
    REFRESH_TOKEN_EXPIRE_DAYS: int = 1000

settings = Settings()