from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Clinic, ClinicCreate

router = APIRouter()

# Create a new clinic
@router.post("/clinics/", response_model=Clinic)
def create_clinic(clinic: ClinicCreate, db: Session = Depends(get_db)):
    db_clinic = Clinic(**clinic.dict())
    db.add(db_clinic)
    db.commit()
    db.refresh(db_clinic)
    return db_clinic

# Get a clinic by ID
@router.get("/clinics/{clinic_id}", response_model=Clinic)
def read_clinic(clinic_id: int, db: Session = Depends(get_db)):
    db_clinic = db.query(Clinic).filter(Clinic.id == clinic_id).first()
    if db_clinic is None:
        raise HTTPException(status_code=404, detail="Clinic not found")
    return db_clinic

# Get all clinics
@router.get("/clinics/", response_model=list[Clinic])
def read_clinics(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    clinics = db.query(Clinic).offset(skip).limit(limit).all()
    return clinics

# Update a clinic by ID
@router.put("/clinics/{clinic_id}", response_model=Clinic)
def update_clinic(clinic_id: int, clinic: ClinicCreate, db: Session = Depends(get_db)):
    db_clinic = db.query(Clinic).filter(Clinic.id == clinic_id).first()
    if db_clinic is None:
        raise HTTPException(status_code=404, detail="Clinic not found")

    for key, value in clinic.dict().items():
        setattr(db_clinic, key, value)

    db.commit()
    db.refresh(db_clinic)
    return db_clinic

# Delete a clinic by ID
@router.delete("/clinics/{clinic_id}", response_model=Clinic)
def delete_clinic(clinic_id: int, db: Session = Depends(get_db)):
    db_clinic = db.query(Clinic).filter(Clinic.id == clinic_id).first()
    if db_clinic is None:
        raise HTTPException(status_code=404, detail="Clinic not found")
    
    db.delete(db_clinic)
    db.commit()
    
    return db_clinic
