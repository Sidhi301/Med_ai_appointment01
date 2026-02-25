from pydantic import BaseModel,EmailStr, Field
from enum import Enum

class DoctorBase(BaseModel):

    name:str
    specialization:str
    experience:int
    fees:int
    available_dates:str
    available_time:str

class DoctorResponse(DoctorBase):
    id:int

    class config:
        orm_mode=True  #he database automatically generates the id when the record is inserted.

