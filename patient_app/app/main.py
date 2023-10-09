from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .database import Base, engine
from .routers import patient, clinic

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    try:
        yield db()
    finally:
        db().close()

# Include the patient and clinic routers
app.include_router(patient.router)
app.include_router(clinic.router)