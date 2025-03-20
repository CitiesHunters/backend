from datetime import timedelta, datetime
import jwt
from app.core.config import settings
from app.core.security import pwd_context
from app.models.user import User
from typing import Tuple

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_token(data: dict, expires_delta: timedelta) -> str:
    """Generates a JWT token"""
    to_encode = data.copy()
    expire = datetime.now() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def generate_token(user: User) -> Tuple[str, str]:
    """Generates a token"""
    access_token = create_token({"sub": user.email}, timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    refresh_token = create_token({"sub": user.email}, timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS))
    return access_token, refresh_token

