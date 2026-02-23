from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import schema
from sqlalchemy.orm import Session
from database.database import get_db,SessionLocal
from schemas.schemas import UserCreate, UserLogin, Token

from models.models import User
from password_hashing.hashed_pw import hash_password, verify_hashed_password, create_access_token



from database.database import SessionLocal
#why this is use :
#this is used to create a router for authentication related endpoints. It allows us to group all authentication related routes under a common prefix ("/auth") and tag them for better organization and documentation in the API. This way, we can easily manage and maintain our authentication routes separately from other parts of the application.

router=APIRouter(
    prefix="/auth",
    tags=["authentication"]
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

#<---------------------------------for signup--------------------------------------->
@router.post("/signup")
def signup(user:UserCreate,db:Session=Depends(get_db)):
    existing_user=db.query(User).filter(User.email==user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email already registered")
    hashed_pw=hash_password(user.password)
    new_user=User(
        name=user.name,
        email=user.email,
        password=hashed_pw,
        role=user.role

    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"User created successfully"}

#<---------------------------------for login--------------------------------------->
@router.post("/login")
def login(user:UserLogin,db:Session=Depends(get_db)):
    existing_user=db.query(User).filter(User.email==user.email).first()
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid email or password")
    if not verify_hashed_password(user.password,existing_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid email or password")
    access_token=create_access_token(
        data={"sub":existing_user.email,"role":existing_user.role}

    )
    return {"access_token":access_token,"token_type":"bearer"}

