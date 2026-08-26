from passlib.context import CryptContext
from jose import jwt, JWTError

ALGORITHM = "HS256"
KEY = "MX565"  # Actual secret key
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time in minutes

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash the password using bcrypt
def hash_password(password: str):
    return pwd_context.hash(password)

# Verify the password against the hashed password
def password_verify(plain_password: str, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, KEY, algorithm= ALGORITHM)