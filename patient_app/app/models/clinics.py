from sqlalchemy import Column, Integer, String
from ..database import Base

# Define the Clinic model
class Clinic(Base):
    __tablename__ = "clinics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    working_hours = Column(String)
    status = Column(bool, default=False)