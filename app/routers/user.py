from app.core.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.auth import UserRegistration
from app.services.auth import get_user_from_token
from fastapi.security import HTTPAuthorizationCredentials
from app.core.security import auth_scheme
from fastapi import Security

user_router = APIRouter(prefix="/api/user", tags=["Users"])

@user_router.get("/me", response_model=UserRegistration)
async def refresh_token(credentials: HTTPAuthorizationCredentials = Security(auth_scheme), db: Session = Depends(get_db)) -> UserRegistration:
    """
    Endpoint di test per ottenere i dati dell'utente loggato.
    Verifica se il token JWT funziona correttamente.
    """
    return get_user_from_token(credentials.credentials, db)
