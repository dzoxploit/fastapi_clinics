from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..controllers import patient_controller
from ..models import patient as patient_model

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new patient
@router.post("/patients/", response_model=patient_model.Patient)
def create_patient(patient_data: patient_model.Patient, db: Session = Depends(get_db)):
    return patient_controller.create_patient(db, patient_data)

# Get a patient by ID
@router.get("/patients/{patient_id}", response_model=patient_model.Patient)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = patient_controller.get_patient(db, patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

# Get all patients
@router.get("/patients/", response_model=list[patient_model.Patient])
def read_patients(db: Session = Depends(get_db)):
    return patient_controller.get_all_patients(db)

# Update a patient by ID
@router.put("/patients/{patient_id}", response_model=patient_model.Patient)
def update_patient(patient_id: int, patient_data: patient_model.Patient, db: Session = Depends(get_db)):
    db_patient = patient_controller.update_patient(db, patient_id, patient_data)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

# Delete a patient by ID
@router.delete("/patients/{patient_id}", response_model=patient_model.Patient)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = patient_controller.delete_patient(db, patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient
