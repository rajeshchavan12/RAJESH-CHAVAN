import database

def print_menu():
    """Prints the main menu options."""
    print("\n--- Pathology Lab Software ---")
    print("1. Add Patient")
    print("2. Add Test for Patient")
    print("3. View All Patients")
    print("4. View Patient Details")
    print("5. Exit")
    print("----------------------------")

def add_patient_ui():
    """UI for adding a new patient."""
    name = input("Enter patient name: ")
    while True:
        try:
            age_input = input("Enter patient age: ")
            age = int(age_input)
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for age.")

    gender = input("Enter patient gender: ")
    patient_id = database.add_patient(name, age, gender)
    if patient_id is not None:
        print(f"Patient added successfully with ID: {patient_id}")
    else:
        print("Error: Failed to add patient.")


def add_test_ui():
    """UI for adding a new test."""
    try:
        patient_id_input = input("Enter patient ID: ")
        patient_id = int(patient_id_input)

        patient = database.get_patient_by_id(patient_id)
        if not patient:
            print("Error: Patient not found or database is inaccessible.")
            return

        test_name = input("Enter test name: ")
        test_result = input("Enter test result: ")
        if database.add_test_for_patient(patient_id, test_name, test_result):
            print("Test added successfully.")
        else:
            print("Error: Could not add test. Patient may not exist or database is inaccessible.")
    except ValueError:
        print("Error: Invalid Patient ID. Please enter a number.")


def view_all_patients_ui():
    """UI for viewing all patients."""
    patients = database.get_all_patients()
    if not patients:
        print("No patients found or database is inaccessible.")
        return
    print("\n--- All Patients ---")
    for patient_id, details in patients.items():
        print(f"ID: {patient_id}, Name: {details['name']}, Age: {details['age']}, Gender: {details['gender']}")
    print("--------------------")

def view_patient_details_ui():
    """UI for viewing a single patient's details."""
    try:
        patient_id_input = input("Enter patient ID: ")
        patient_id = int(patient_id_input)
        patient = database.get_patient_by_id(patient_id)
        if patient:
            print(f"\n--- Patient Details (ID: {patient_id}) ---")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Gender: {patient['gender']}")
            print("Tests:")
            if patient.get('tests'):
                for test in patient['tests']:
                    print(f"  - {test['name']}: {test['result']}")
            else:
                print("  No tests found for this patient.")
            print("---------------------------------")
        else:
            print("Error: Patient not found or database is inaccessible.")
    except ValueError:
        print("Error: Invalid Patient ID. Please enter a number.")


def main():
    """Main function to run the application."""
    database.initialize_database()
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_patient_ui()
        elif choice == '2':
            add_test_ui()
        elif choice == '3':
            view_all_patients_ui()
        elif choice == '4':
            view_patient_details_ui()
        elif choice == '5':
            print("Exiting application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
