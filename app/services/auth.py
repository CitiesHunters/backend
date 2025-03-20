import jwt
from app.core.config import settings
from fastapi import HTTPException
from app.models.user import User
from sqlalchemy.orm import Session

def validate_token(token: str) -> dict:
    """Validates a token"""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Generic Error : {e}")
    
def get_user_from_token(token: str, db: Session) -> dict:
    """Extracts the user from a token"""
    
    email = validate_token(token).get("sub")
    existing_user = db.query(User).filter(User.email == email).first()
    if not existing_user:
        raise HTTPException(status_code=400, detail="User not found")
    return existing_user