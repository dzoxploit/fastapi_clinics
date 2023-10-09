from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.fixture
def sample_patient_data():
    return {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "address": "123 Main St",
        "phone_number": "+1234567890",
        "birthplace": "City",
        "date_of_birth": "1990-01-01",
        "description": "Test patient",
    }

def test_create_patient(sample_patient_data):
    response = client.post("/patients/", json=sample_patient_data)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == sample_patient_data["name"]
    assert data["email"] == sample_patient_data["email"]
    # Add more assertions for other fields as needed

def test_read_patient():
    # Assuming you have a valid patient ID for testing
    patient_id = 1
    response = client.get(f"/patients/{patient_id}")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "email" in data
    # Add more assertions for other fields as needed

def test_update_patient(sample_patient_data):
    # Assuming you have a valid patient ID for testing
    patient_id = 1
    updated_data = {"name": "Updated Name"}
    response = client.put(f"/patients/{patient_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == updated_data["name"]

def test_delete_patient():
    # Assuming you have a valid patient ID for testing
    patient_id = 1
    response = client.delete(f"/patients/{patient_id}")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "email" in data
    # Add more assertions for other fields as needed

if __name__ == "__main__":
    pytest.main(["-sv", "test_client.py"])
