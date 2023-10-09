from sqlalchemy import Column, Integer, String, Date, Text
from ..database import Base

# Define the Patient model
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    address = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    birthplace = Column(String, nullable=True)  # Nullable birthplace
    date_of_birth = Column(Date, nullable=True)  # Nullable tanggal_lahir
    description = Column(Text, nullable=True)  # N