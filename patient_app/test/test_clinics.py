from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.fixture
def sample_clinic_data():
    return {
        "name": "Example Clinic",
        "address": "123 Clinic St",
        "working_hours": "9:00 AM - 5:00 PM",
        "status": False
    }

def test_create_clinic(sample_clinic_data):
    response = client.post("/clinics/", json=sample_clinic_data)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == sample_clinic_data["name"]
    assert data["address"] == sample_clinic_data["address"]
    assert data["working_hours"] == sample_clinic_data["working_hours"]
    assert data["status"] == sample_clinic_data["status"]

def test_read_clinic():
    # Assuming you have a valid clinic ID for testing
    clinic_id = 1
    response = client.get(f"/clinics/{clinic_id}")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "address" in data
    assert "working_hours" in data
    assert "status" in data

def test_update_clinic(sample_clinic_data):
    # Assuming you have a valid clinic ID for testing
    clinic_id = 1
    updated_data = {"name": "Updated Clinic Name"}
    response = client.put(f"/clinics/{clinic_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == updated_data["name"]

def test_delete_clinic():
    # Assuming you have a valid clinic ID for testing
    clinic_id = 1
    response = client.delete(f"/clinics/{clinic_id}")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "address" in data
    assert "working_hours" in data
    assert "status" in data

if __name__ == "__main__":
    pytest.main(["-sv", "test_clinics.py"])
