from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import schema
from sqlalchemy.orm import Session
from database.database import get_db,SessionLocal
from schemas.schemas import  Token
from schemas.doctor import DoctorResponse
from models.models import Doctor
router=APIRouter()

@router.get("/doctors",response_model=list[DoctorResponse])
def get_doc(db:Session=Depends(get_db)):
    return db.query(Doctor)