import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.patient import Patient

class TestPatient(unittest.TestCase):
    """Unit tests for the Patient class."""

    def test_patient_creation(self):
        """Test that a Patient object is created with the correct attributes."""
        patient = Patient(1, "John Doe", 30, "Male", "123-456-7890")
        self.assertEqual(patient.patient_id, 1)
        self.assertEqual(patient.name, "John Doe")
        self.assertEqual(patient.age, 30)
        self.assertEqual(patient.gender, "Male")
        self.assertEqual(patient.contact, "123-456-7890")

    def test_patient_str(self):
        """Test the string representation of a Patient object."""
        patient = Patient(1, "John Doe", 30, "Male", "123-456-7890")
        expected_str = "Patient ID: 1, Name: John Doe, Age: 30, Gender: Male, Contact: 123-456-7890"
        self.assertEqual(str(patient), expected_str)

if __name__ == '__main__':
    unittest.main()
