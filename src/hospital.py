import csv
import os
from src.patient import Patient
from src.doctor import Doctor
from src.appointment import Appointment

class Hospital:
    """Represents the hospital management system."""

    def __init__(self):
        """Initializes the Hospital, loads data from CSV files if they exist."""
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.next_patient_id = 1
        self.next_doctor_id = 1
        self.next_appointment_id = 1

        self.patients_csv = 'data/patients.csv'
        self.doctors_csv = 'data/doctors.csv'
        self.appointments_csv = 'data/appointments.csv'

        self.load_data()

    def load_data(self):
        self._load_patients()
        self._load_doctors()
        self._load_appointments()

    def _load_patients(self):
        if not os.path.exists(self.patients_csv):
            return
        with open(self.patients_csv, mode='r', newline='') as file:
            reader = csv.reader(file)
            try:
                next(reader) # Skip header
                for row in reader:
                    patient = Patient(int(row[0]), row[1], int(row[2]), row[3], row[4])
                    self.patients.append(patient)
                    self.next_patient_id = max(self.next_patient_id, int(row[0]) + 1)
            except StopIteration:
                pass # File is empty

    def _load_doctors(self):
        if not os.path.exists(self.doctors_csv):
            return
        with open(self.doctors_csv, mode='r', newline='') as file:
            reader = csv.reader(file)
            try:
                next(reader) # Skip header
                for row in reader:
                    doctor = Doctor(int(row[0]), row[1], row[2], row[3])
                    self.doctors.append(doctor)
                    self.next_doctor_id = max(self.next_doctor_id, int(row[0]) + 1)
            except StopIteration:
                pass # File is empty

    def _load_appointments(self):
        if not os.path.exists(self.appointments_csv):
            return
        with open(self.appointments_csv, mode='r', newline='') as file:
            reader = csv.reader(file)
            try:
                next(reader) # Skip header
                for row in reader:
                    appointment_id, patient_id, doctor_id, date, time = row
                    patient = self.search_patient_by_id(int(patient_id))
                    doctor = self.search_doctor_by_id(int(doctor_id))
                    if patient and doctor:
                        appointment = Appointment(int(appointment_id), patient, doctor, date, time)
                        self.appointments.append(appointment)
                        self.next_appointment_id = max(self.next_appointment_id, int(appointment_id) + 1)
            except StopIteration:
                pass # File is empty

    def save_data(self):
        self._save_patients()
        self._save_doctors()
        self._save_appointments()

    def _save_patients(self):
        with open(self.patients_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['patient_id', 'name', 'age', 'gender', 'contact'])
            for patient in self.patients:
                writer.writerow([patient.patient_id, patient.name, patient.age, patient.gender, patient.contact])

    def _save_doctors(self):
        with open(self.doctors_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['doctor_id', 'name', 'specialization', 'contact'])
            for doctor in self.doctors:
                writer.writerow([doctor.doctor_id, doctor.name, doctor.specialization, doctor.contact])

    def _save_appointments(self):
        with open(self.appointments_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['appointment_id', 'patient_id', 'doctor_id', 'date', 'time'])
            for appointment in self.appointments:
                writer.writerow([appointment.appointment_id, appointment.patient.patient_id, appointment.doctor.doctor_id, appointment.date, appointment.time])

    def add_patient(self, name, age, gender, contact):
        """Adds a new patient to the hospital."""
        patient = Patient(self.next_patient_id, name, age, gender, contact)
        self.patients.append(patient)
        self.next_patient_id += 1
        return patient

    def view_patients(self):
        """Returns a list of all patients."""
        return self.patients

    def search_patient_by_id(self, patient_id):
        """Searches for a patient by their ID."""
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None

    def delete_patient(self, patient_id):
        """Deletes a patient by their ID."""
        patient = self.search_patient_by_id(patient_id)
        if patient:
            self.patients.remove(patient)
            return True
        return False

    def add_doctor(self, name, specialization, contact):
        """Adds a new doctor to the hospital."""
        doctor = Doctor(self.next_doctor_id, name, specialization, contact)
        self.doctors.append(doctor)
        self.next_doctor_id += 1
        return doctor

    def view_doctors(self):
        """Returns a list of all doctors."""
        return self.doctors

    def search_doctor_by_id(self, doctor_id):
        """Searches for a doctor by their ID."""
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return doctor
        return None

    def delete_doctor(self, doctor_id):
        """Deletes a doctor by their ID."""
        doctor = self.search_doctor_by_id(doctor_id)
        if doctor:
            self.doctors.remove(doctor)
            return True
        return False

    def book_appointment(self, patient_id, doctor_id, date, time):
        """Books a new appointment."""
        patient = self.search_patient_by_id(patient_id)
        doctor = self.search_doctor_by_id(doctor_id)
        if patient and doctor:
            appointment = Appointment(self.next_appointment_id, patient, doctor, date, time)
            self.appointments.append(appointment)
            self.next_appointment_id += 1
            return appointment
        return None

    def view_appointments(self):
        """Returns a list of all appointments."""
        return self.appointments
