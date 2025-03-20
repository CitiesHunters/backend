from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class UserRegistration(BaseModel):
    """Schema for user registration with all attributes."""
    phone_number: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: EmailStr
    password: str
    birth_date: Optional[date] = None
    custom_tag: Optional[str] = None

class TokenResponse(BaseModel):
    """Schema for token response."""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class UserLogin(BaseModel):
    """Schema for user login."""
    email: EmailStr
    password: str