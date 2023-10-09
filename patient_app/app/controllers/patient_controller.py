from sqlalchemy.orm import Session
from ..models import patient

# Create a new patient
def create_patient(db: Session, patient_data: dict):
    db_patient = patient.Patient(**patient_data)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

# Get a patient by ID
def get_patient(db: Session, patient_id: int):
    return db.query(patient.Patient).filter(patient.Patient.id == patient_id).first()

# Get all patients
def get_all_patients(db: Session):
    return db.query(patient.Patient).all()

# Update a patient
def update_patient(db: Session, patient_id: int, patient_data: dict):
    db_patient = db.query(patient.Patient).filter(patient.Patient.id == patient_id).first()
    if db_patient:
        for key, value in patient_data.items():
            setattr(db_patient, key, value)
        db.commit()
        db.refresh(db_patient)
    return db_patient

# Delete a patient by ID
def delete_patient(db: Session, patient_id: int):
    db_patient = db.query(patient.Patient).filter(patient.Patient.id == patient_id).first()
    if db_patient:
        db.delete(db_patient)
        db.commit()
    return db_patient