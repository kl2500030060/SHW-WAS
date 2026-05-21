
import json
import os

PATIENTS_FILE = "data/patients.json"

def save_patient(patient_dict):
    """Saves or updates a patient record in the JSON database."""
    os.makedirs("data", exist_ok=True)
    patients = load_all_patients()
    

    patients[patient_dict["patient_id"]] = patient_dict
    
    try:
        with open(PATIENTS_FILE, 'w') as f:
            json.dump(patients, f, indent=4)
    except IOError as e:
        print(f"CRITICAL ERROR: Failed to write to {PATIENTS_FILE}. Details: {e}")

def load_all_patients():
    """Loads all patients from the JSON file."""
    if not os.path.exists(PATIENTS_FILE):
        return {}
    
    try:
        with open(PATIENTS_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):

        return {}

def get_patient(patient_id):
    """Retrieves a specific patient by ID."""
    patients = load_all_patients()
    return patients.get(patient_id)
