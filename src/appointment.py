from src.patient import Patient
from src.doctor import Doctor

class Appointment:
    """Represents an appointment in the hospital."""

    def __init__(self, appointment_id, patient, doctor, date, time):
        """
        Initializes an Appointment object.

        Args:
            appointment_id (int): The unique ID of the appointment.
            patient (Patient): The patient for the appointment.
            doctor (Doctor): The doctor for the appointment.
            date (str): The date of the appointment.
            time (str): The time of the appointment.
        """
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def __str__(self):
        """Returns a string representation of the appointment."""
        return f"Appointment ID: {self.appointment_id}, Date: {self.date}, Time: {self.time}\\n  Patient: {self.patient.name}\\n  Doctor: {self.doctor.name}"
