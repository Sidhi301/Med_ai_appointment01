from pydantic import BaseModel,EmailStr, Field
from enum import Enum
from datetime import datetime

class UserSimple(BaseModel):
    id: int
    name:str
    class Config:
        from_attribute=True


class DoctorSimple(BaseModel):
    id:int
    name:str
    specialization:str

    class Config:
        from_attribute=True


# appointment creation

class appointmentCreate(BaseModel):
    id:int
    appointment_time:datetime
    reason:str
    status:str

    patient: UserSimple
    doctor:DoctorSimple
    class config :
        from_attributes=True

