import enum# enum limits a vakue to a fixed ,allowed set


from sqlalchemy import Column, Integer, String,ForeignKey,DateTime,Boolean,Enum
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