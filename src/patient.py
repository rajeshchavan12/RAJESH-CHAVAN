class Patient:
    """Represents a patient in the hospital."""

    def __init__(self, patient_id, name, age, gender, contact):
        """
        Initializes a Patient object.

        Args:
            patient_id (int): The unique ID of the patient.
            name (str): The name of the patient.
            age (int): The age of the patient.
            gender (str): The gender of the patient.
            contact (str): The contact information of the patient.
        """
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact

    def __str__(self):
        """Returns a string representation of the patient."""
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Contact: {self.contact}"
