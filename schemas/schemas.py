from pydantic import BaseModel,EmailStr, Field
from enum import Enum

class role(str,Enum):
    admin="admin",
    doctor="doctor",
    patient="patient"
class UserCreate(BaseModel):
    name:str
    email:EmailStr
    password:str
    role:role
class UserLogin(BaseModel):
    email:EmailStr
    password: str = Field(min_length=8, max_length=64)
class Token(BaseModel):
    access_token:str
    token_type:str


