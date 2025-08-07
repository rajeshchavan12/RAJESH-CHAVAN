import json
import os

DB_FILE = 'pathology.json'

def initialize_database():
    """Creates the database file if it doesn't exist."""
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as f:
            json.dump({'patients': {}, 'next_patient_id': 1}, f, indent=4)

def _read_db():
    """Reads and parses the JSON database file, handling errors."""
    try:
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Return a default structure on error
        return None

def _write_db(data):
    """Writes data to the JSON database file."""
    try:
        with open(DB_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def get_all_patients():
    """Retrieves all patients from the database."""
    data = _read_db()
    return data.get('patients', {}) if data else {}

def add_patient(name, age, gender):
    """Adds a new patient to the database."""
    data = _read_db()
    if data is None:
        print("Error: Database is inaccessible or corrupted.")
        return None

    patient_id = data.get('next_patient_id', 1)
    if 'patients' not in data:
        data['patients'] = {}

    data['patients'][patient_id] = {
        'name': name,
        'age': age,
        'gender': gender,
        'tests': []
    }
    data['next_patient_id'] = patient_id + 1

    if _write_db(data):
        return patient_id
    else:
        print("Error: Failed to write to the database.")
        return None

def get_patient_by_id(patient_id):
    """Retrieves a single patient by their ID."""
    data = _read_db()
    if data and 'patients' in data:
        return data['patients'].get(str(patient_id))
    return None

def add_test_for_patient(patient_id, test_name, test_result):
    """Adds a new test result for a patient."""
    data = _read_db()
    if data is None or 'patients' not in data:
        print("Error: Database is inaccessible or corrupted.")
        return False

    patient = data['patients'].get(str(patient_id))
    if patient:
        patient['tests'].append({'name': test_name, 'result': test_result})
        return _write_db(data)

    return False
