import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.doctor import Doctor

class TestDoctor(unittest.TestCase):
    """Unit tests for the Doctor class."""

    def test_doctor_creation(self):
        """Test that a Doctor object is created with the correct attributes."""
        doctor = Doctor(1, "Dr. Smith", "Cardiology", "987-654-3210")
        self.assertEqual(doctor.doctor_id, 1)
        self.assertEqual(doctor.name, "Dr. Smith")
        self.assertEqual(doctor.specialization, "Cardiology")
        self.assertEqual(doctor.contact, "987-654-3210")

    def test_doctor_str(self):
        """Test the string representation of a Doctor object."""
        doctor = Doctor(1, "Dr. Smith", "Cardiology", "987-654-3210")
        expected_str = "Doctor ID: 1, Name: Dr. Smith, Specialization: Cardiology, Contact: 987-654-3210"
        self.assertEqual(str(doctor), expected_str)

if __name__ == '__main__':
    unittest.main()
