import unittest
import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.hospital import Hospital

class TestHospital(unittest.TestCase):
    """Unit tests for the Hospital class."""

    def setUp(self):
        """Set up a new hospital instance for each test."""
        # Ensure data files from previous runs are cleaned up
        if os.path.exists('data/patients.csv'):
            os.remove('data/patients.csv')
        if os.path.exists('data/doctors.csv'):
            os.remove('data/doctors.csv')
        if os.path.exists('data/appointments.csv'):
            os.remove('data/appointments.csv')

        self.hospital = Hospital()
        self.hospital.add_patient("John Doe", 30, "Male", "123-456-7890")
        self.hospital.add_doctor("Dr. Smith", "Cardiology", "987-654-3210")

    def tearDown(self):
        """Clean up data files after each test."""
        if os.path.exists('data/patients.csv'):
            os.remove('data/patients.csv')
        if os.path.exists('data/doctors.csv'):
            os.remove('data/doctors.csv')
        if os.path.exists('data/appointments.csv'):
            os.remove('data/appointments.csv')

    def test_add_patient(self):
        """Test adding a patient."""
        self.assertEqual(len(self.hospital.patients), 1)
        self.assertEqual(self.hospital.patients[0].name, "John Doe")

    def test_add_doctor(self):
        """Test adding a doctor."""
        self.assertEqual(len(self.hospital.doctors), 1)
        self.assertEqual(self.hospital.doctors[0].name, "Dr. Smith")

    def test_search_patient_by_id(self):
        """Test searching for a patient by ID."""
        patient = self.hospital.search_patient_by_id(1)
        self.assertIsNotNone(patient)
        self.assertEqual(patient.name, "John Doe")
        self.assertIsNone(self.hospital.search_patient_by_id(99))

    def test_search_doctor_by_id(self):
        """Test searching for a doctor by ID."""
        doctor = self.hospital.search_doctor_by_id(1)
        self.assertIsNotNone(doctor)
        self.assertEqual(doctor.name, "Dr. Smith")
        self.assertIsNone(self.hospital.search_doctor_by_id(99))

    def test_delete_patient(self):
        """Test deleting a patient."""
        self.assertTrue(self.hospital.delete_patient(1))
        self.assertEqual(len(self.hospital.patients), 0)
        self.assertFalse(self.hospital.delete_patient(99))

    def test_delete_doctor(self):
        """Test deleting a doctor."""
        self.assertTrue(self.hospital.delete_doctor(1))
        self.assertEqual(len(self.hospital.doctors), 0)
        self.assertFalse(self.hospital.delete_doctor(99))

    def test_book_appointment(self):
        """Test booking an appointment."""
        appointment = self.hospital.book_appointment(1, 1, "2024-12-25", "10:00")
        self.assertIsNotNone(appointment)
        self.assertEqual(len(self.hospital.appointments), 1)
        self.assertEqual(appointment.patient.name, "John Doe")
        self.assertEqual(appointment.doctor.name, "Dr. Smith")
        self.assertIsNone(self.hospital.book_appointment(99, 1, "2024-12-25", "10:00"))
        self.assertIsNone(self.hospital.book_appointment(1, 99, "2024-12-25", "10:00"))

    def test_data_persistence(self):
        """Test saving and loading data."""
        self.hospital.book_appointment(1, 1, "2024-12-25", "10:00")
        self.hospital.save_data()

        # Create a new hospital instance to load the data
        new_hospital = Hospital()
        self.assertEqual(len(new_hospital.patients), 1)
        self.assertEqual(len(new_hospital.doctors), 1)
        self.assertEqual(len(new_hospital.appointments), 1)
        self.assertEqual(new_hospital.patients[0].name, "John Doe")
        self.assertEqual(new_hospital.doctors[0].name, "Dr. Smith")
        self.assertEqual(new_hospital.appointments[0].date, "2024-12-25")

if __name__ == '__main__':
    unittest.main()
