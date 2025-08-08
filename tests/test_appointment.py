import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.patient import Patient
from src.doctor import Doctor
from src.appointment import Appointment

class TestAppointment(unittest.TestCase):
    """Unit tests for the Appointment class."""

    def test_appointment_creation(self):
        """Test that an Appointment object is created with the correct attributes."""
        patient = Patient(1, "John Doe", 30, "Male", "123-456-7890")
        doctor = Doctor(1, "Dr. Smith", "Cardiology", "987-654-3210")
        appointment = Appointment(1, patient, doctor, "2024-12-25", "10:00")
        self.assertEqual(appointment.appointment_id, 1)
        self.assertEqual(appointment.patient, patient)
        self.assertEqual(appointment.doctor, doctor)
        self.assertEqual(appointment.date, "2024-12-25")
        self.assertEqual(appointment.time, "10:00")

    def test_appointment_str(self):
        """Test the string representation of an Appointment object."""
        patient = Patient(1, "John Doe", 30, "Male", "123-456-7890")
        doctor = Doctor(1, "Dr. Smith", "Cardiology", "987-654-3210")
        appointment = Appointment(1, patient, doctor, "2024-12-25", "10:00")
        expected_str = "Appointment ID: 1, Date: 2024-12-25, Time: 10:00\\n  Patient: John Doe\\n  Doctor: Dr. Smith"
        self.assertEqual(str(appointment), expected_str)

if __name__ == '__main__':
    unittest.main()
