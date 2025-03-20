from app.core.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import UserRegistration, TokenResponse, UserLogin
from app.models.user import User
from app.utils.auth import get_password_hash, verify_password, generate_token
from app.services.auth import get_user_from_token
from fastapi.security import HTTPAuthorizationCredentials
from app.core.security import auth_scheme
from fastapi import Security

authentication_router = APIRouter(prefix="/api/auth", tags=["Authentication"])

@authentication_router.post("/register", response_model=TokenResponse)
async def register(user: UserRegistration, db: Session = Depends(get_db)) -> TokenResponse:
    """
    Registra un nuovo utente nel database e restituisce un token di accesso e un token di refresh.
    """
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user.password = get_password_hash(user.password)

    User.create(user, db)
    access_token, refresh_token = generate_token(user)

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@authentication_router.post("/login", response_model=TokenResponse)
async def login(user: UserLogin, db: Session = Depends(get_db)) -> TokenResponse:
    """
    Logga un utente e restituisce un token di accesso e un token di refresh.
    """
    existing_user = db.query(User).filter(User.email == user.email).first()

    if not existing_user:
        raise HTTPException(status_code=400, detail="Email not registered")
    if not verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    access_token, refresh_token = generate_token(existing_user)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@authentication_router.get("/refresh_token", response_model=TokenResponse)
async def refresh_token(credentials: HTTPAuthorizationCredentials = Security(auth_scheme), db: Session = Depends(get_db)) -> TokenResponse:
    """
    Logga un utente e restituisce un token di accesso e un token di refresh.
    """
    existing_user = get_user_from_token(credentials.credentials, db)
    access_token, refresh_token = generate_token(existing_user)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}
