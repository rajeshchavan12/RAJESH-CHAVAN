class Doctor:
    """Represents a doctor in the hospital."""

    def __init__(self, doctor_id, name, specialization, contact):
        """
        Initializes a Doctor object.

        Args:
            doctor_id (int): The unique ID of the doctor.
            name (str): The name of the doctor.
            specialization (str): The specialization of the doctor.
            contact (str): The contact information of the doctor.
        """
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.contact = contact

    def __str__(self):
        """Returns a string representation of the doctor."""
        return f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}, Contact: {self.contact}"
