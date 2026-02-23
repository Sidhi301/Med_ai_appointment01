import hashlib
from passlib.context import CryptContext
pwd_content=CryptContext(schemes=["bcrypt"],deprecated="auto")
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from jose import JWTError, jwt
load_dotenv()
SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def hash_password(password:str)->str:
    sha=hashlib.sha256(password.encode("utf-8")).hexdigest()
    return pwd_content.hash(sha)
#SHA-256 converts any-length password into a fixed 32-byte value so bcrypt never truncates input at 72 bytes.

def verify_hashed_password(plain_password:str,hashed_password:str)->bool:
    sha = hashlib.sha256(plain_password.encode("utf-8")).hexdigest()
    return pwd_content.verify(sha,hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)