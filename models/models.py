import enum# enum limits a vakue to a fixed ,allowed set


from sqlalchemy import Column, Integer, String,ForeignKey,DateTime,Boolean,Enum,Date,Time
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database.database import Base as Base


class UserRole(str, enum.Enum):
    admin="admin",
    doctor="doctor",
    patient="patient"
class User(Base):
    __tablename__="users"
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(255),nullable=False)
    email=Column(String(255),unique=True,index=True,nullable=False)
    password=Column(String(255),nullable=False)
    role=Column(Enum(UserRole),default=UserRole.patient,nullable=False)
    appointments=relationship("Appointment",back_populates="patient")

    
class Doctor(Base):
    __tablename__="doctors"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(255),nullable=False)
    specialization=Column(String(255),nullable=False)
    experience=Column(Integer,nullable=False)
    fees=Column(Integer,nullable=False)
    available_dates=Column(String(255),nullable=False)
    available_time=Column(String(255),nullable=False)
    appointments=relationship("Appointment",back_populates="doctor")


class Appointment(Base):
    __tablename__="appointment"
    id=Column(Integer,primary_key=True,nullable=False)
    patient_id=Column(Integer,ForeignKey("users.id"))
    doctor_id=Column(Integer,ForeignKey("doctors.id"))
    appointment_date=Column(Date,nullable=False)
    appointment_time=Column(Time,nullable=False)
    status=Column(String(50),default="pending")
    patient=relationship("User",back_populates="appointments")
    doctor=relationship("Doctor",back_populates="appointments")



