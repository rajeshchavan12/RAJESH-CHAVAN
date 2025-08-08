from src.hospital import Hospital

def patient_menu(hospital):
    """Displays the patient management menu and handles user input."""
    while True:
        print("\\n--- Patient Management ---")
        print("1. Add a new patient")
        print("2. View all patients")
        print("3. Search for a patient by ID")
        print("4. Delete a patient")
        print("5. Back to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter patient's name: ")
            age = int(input("Enter patient's age: "))
            gender = input("Enter patient's gender: ")
            contact = input("Enter patient's contact: ")
            patient = hospital.add_patient(name, age, gender, contact)
            print(f"Patient added successfully with ID: {patient.patient_id}")
        elif choice == '2':
            patients = hospital.view_patients()
            if patients:
                for patient in patients:
                    print(patient)
            else:
                print("No patients found.")
        elif choice == '3':
            patient_id = int(input("Enter patient ID: "))
            patient = hospital.search_patient_by_id(patient_id)
            if patient:
                print(patient)
            else:
                print("Patient not found.")
        elif choice == '4':
            patient_id = int(input("Enter patient ID: "))
            if hospital.delete_patient(patient_id):
                print("Patient deleted successfully.")
            else:
                print("Patient not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def doctor_menu(hospital):
    """Displays the doctor management menu and handles user input."""
    while True:
        print("\\n--- Doctor Management ---")
        print("1. Add a new doctor")
        print("2. View all doctors")
        print("3. Search for a doctor by ID")
        print("4. Delete a doctor")
        print("5. Back to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter doctor's name: ")
            specialization = input("Enter doctor's specialization: ")
            contact = input("Enter doctor's contact: ")
            doctor = hospital.add_doctor(name, specialization, contact)
            print(f"Doctor added successfully with ID: {doctor.doctor_id}")
        elif choice == '2':
            doctors = hospital.view_doctors()
            if doctors:
                for doctor in doctors:
                    print(doctor)
            else:
                print("No doctors found.")
        elif choice == '3':
            doctor_id = int(input("Enter doctor ID: "))
            doctor = hospital.search_doctor_by_id(doctor_id)
            if doctor:
                print(doctor)
            else:
                print("Doctor not found.")
        elif choice == '4':
            doctor_id = int(input("Enter doctor ID: "))
            if hospital.delete_doctor(doctor_id):
                print("Doctor deleted successfully.")
            else:
                print("Doctor not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def appointment_menu(hospital):
    """Displays the appointment management menu and handles user input."""
    while True:
        print("\\n--- Appointment Management ---")
        print("1. Book a new appointment")
        print("2. View all appointments")
        print("3. Back to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            patient_id = int(input("Enter patient ID: "))
            doctor_id = int(input("Enter doctor ID: "))
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            appointment = hospital.book_appointment(patient_id, doctor_id, date, time)
            if appointment:
                print(f"Appointment booked successfully with ID: {appointment.appointment_id}")
            else:
                print("Could not book appointment. Please check patient and doctor IDs.")
        elif choice == '2':
            appointments = hospital.view_appointments()
            if appointments:
                for appointment in appointments:
                    print(appointment)
            else:
                print("No appointments found.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    """The main function of the hospital management system."""
    hospital = Hospital()
    while True:
        print("\\n--- Hospital Management System ---")
        print("1. Manage Patients")
        print("2. Manage Doctors")
        print("3. Manage Appointments")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            patient_menu(hospital)
        elif choice == '2':
            doctor_menu(hospital)
        elif choice == '3':
            appointment_menu(hospital)
        elif choice == '4':
            hospital.save_data()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
