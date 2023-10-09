from sqlalchemy.orm import Session
from ..models import clinic

# Create a new clinic
def create_clinic(db: Session, clinic_data: dict):
    db_clinic = clinic.Clinic(**clinic_data)
    db.add(db_clinic)
    db.commit()
    db.refresh(db_clinic)
    return db_clinic

# Get a clinic by ID
def get_clinic(db: Session, clinic_id: int):
    return db.query(clinic.Clinic).filter(clinic.Clinic.id == clinic_id).first()

# Get all clinics
def get_all_clinics(db: Session):
    return db.query(clinic.Clinic).all()

# Update a clinic
def update_clinic(db: Session, clinic_id: int, clinic_data: dict):
    db_clinic = db.query(clinic.Clinic).filter(clinic.Clinic.id == clinic_id).first()
    if db_clinic:
        for key, value in clinic_data.items():
            setattr(db_clinic, key, value)
        db.commit()
        db.refresh(db_clinic)
    return db_clinic

# Delete a clinic by ID
def delete_clinic(db: Session, clinic_id: int):
    db_clinic = db.query(clinic.Clinic).filter(clinic.Clinic.id == clinic_id).first()
    if db_clinic:
        db.delete(db_clinic)
        db.commit()
    return db_clinic