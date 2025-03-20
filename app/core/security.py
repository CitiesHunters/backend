from fastapi.security import HTTPBearer
from passlib.context import CryptContext

auth_scheme = HTTPBearer()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
