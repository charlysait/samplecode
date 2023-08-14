# Define a class for managing doctors' information
class Doctor:
    def __init__(self, id, name, specialist, timing, qualification, room_number):
        self.id = id
        self.name = name
        self.specialist = specialist
        self.timing = timing
        self.qualification = qualification
        self.room_number = room_number


# Define a class for hospital facilities
class Facility:
    def __init__(self, name):
        self.name = name


# Define a class for laboratory facilities
class Laboratory:
    def __init__(self, facility, cost):
        self.facility = facility
        self.cost = cost


# Define a class for managing patient information
class Patient:
    def __init__(self, id, name, disease, gender, age):
        self.id = id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age


# Define a class for the hospital management system
class HospitalManagementSystem:
    def __init__(self):
        # Initialize lists to store data
        self.doctors = []
        self.facilities = []
        self.laboratories = []
        self.patients = []

    # Display list of doctors and their details
    def display_doctors(self):
        # Print column headers
        print(
            "{:>4}  {:<10}  {:<12}  {:<9}  {:<15}  {:<7}".format("id", "name", "specialist", "timing", "qualification",
                                                                 "roomNb"))
        print("-" * 53)
        # Print doctor details
        for doctor in self.doctors:
            print("{:>4}  {:<10}  {:<12}  {:<9}  {:<15}  {:<7}".format(doctor.id, doctor.name, doctor.specialist,
                                                                       doctor.timing, doctor.qualification,
                                                                       doctor.room_number))

    # Search for a doctor by ID
    def search_doctor_by_id(self, doctor_id):
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        return None

    # Search for a doctor by name
    def search_doctor_by_name(self, doctor_name):
        for doctor in self.doctors:
            if doctor.name.lower() == doctor_name.lower():
                return doctor
        return None

    # Add a new doctor to the system
    def add_doctor(self, id, name, specialist, timing, qualification, room_number):
        new_doctor = Doctor(id, name, specialist, timing, qualification, room_number)
        self.doctors.append(new_doctor)

    # Edit information of an existing doctor
    def edit_doctor_info(self, doctor_id, name, specialist, timing, qualification, room_number):
        doctor = self.search_doctor_by_id(doctor_id)
        if doctor:
            doctor.name = name
            doctor.specialist = specialist
            doctor.timing = timing
            doctor.qualification = qualification
            doctor.room_number = room_number

    # Display list of hospital facilities
    def display_facilities(self):
        print("Hospital Facilities:")
        print("-" * 25)
        for facility in self.facilities:
            print(facility.name)

    # Add a new facility to the hospital
    def add_facility(self, name):
        new_facility = Facility(name)
        self.facilities.append(new_facility)

    # Display list of laboratory facilities
    def display_laboratories(self):
        print("{:<12}  {:<5}".format("Facility", "Cost"))
        print("-" * 20)
        for lab in self.laboratories:
            print("{:<12}  {:<5}".format(lab.facility, lab.cost))

    # Add a new laboratory facility
    def add_laboratory(self, facility, cost):
        new_lab = Laboratory(facility, cost)
        self.laboratories.append(new_lab)

    # Display list of patients and their details
    def display_patients(self):
        print("{:<4}  {:<20}  {:<15}  {:<10}  {:<6}".format("ID", "Name", "Disease", "Gender", "Age"))
        print("-" * 60)
        for patient in self.patients:
            print(
                "{:<4}  {:<20}  {:<15}  {:<10}  {:<6}".format(patient.id, patient.name, patient.disease, patient.gender,
                                                              patient.age))

    # Search for a patient by ID
    def search_patient_by_id(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        return None

    # Add a new patient to the hospital
    def add_patient(self, id, name, disease, gender, age):
        new_patient = Patient(id, name, disease, gender, age)
        self.patients.append(new_patient)

    # Edit information of an existing patient
    def edit_patient_info(self, patient_id, name, disease, gender, age):
        patient = self.search_patient_by_id(patient_id)
        if patient:
            patient.name = name
            patient.disease = disease
            patient.gender = gender
            patient.age = age

# Create an instance of the hospital management system
ahms = HospitalManagementSystem()

# Populate initial data into the system
ahms.add_doctor(21, "Dr.Gody", "ENT", "5-11AM", "MBBS,MD", 17)
ahms.add_doctor(32, "Dr.Vikram", "Physician", "10-3AM", "MBBS,MD", 45)
ahms.add_doctor(17, "Dr.Amy", "Surgeon", "8-2AM", "BDM", 8)
ahms.add_doctor(33, "Dr.David", "Artho", "10-4PM", "MBBS,MS", 40)
ahms.add_doctor(123, "Dr.Ross", "Headackes", "8-10am", "Mst", 102)
ahms.add_doctor(66, "Dr.Mike", "Heart", "9am-5pm", "MS", 2)

ahms.add_facility("Ambulance")
ahms.add_facility("Admit Facility")
ahms.add_facility("Canteen")
ahms.add_facility("Emergency")

ahms.add_laboratory("Lab1", 800)
ahms.add_laboratory("Lab2", 1200)
ahms.add_laboratory("Lab3", 500)
ahms.add_laboratory("Lab4", 50)

ahms.add_patient(12, "Pankaj", "Cancer", "Male", 30)
ahms.add_patient(13, "Janina", "Cold", "Female", 23)
ahms.add_patient(14, "Alonna", "Malaria", "Female", 45)
ahms.add_patient(15, "Ravi", "Diabetes", "Male", 65)

# Main menu loop to interact with the system
while True:
    # Display main menu options
    print("\nWelcome to Alberta Hospital (AH) Management system")
    print("Select from the following options, or select 0 to stop:")
    print("1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients\n0 - Exit")

    # Get user's choice
    choice = input()

    # Handle user's choice
    if choice == '1':
        # Doctor menu loop
        while True:
            print("\nDoctors Menu:")
            print(
                "1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu")
            doctor_choice = input()

            # Handle doctor menu choice
            if doctor_choice == '1':
                ahms.display_doctors()
            elif doctor_choice == '2':
                doctor_id = int(input("Enter the doctor ID:\n"))
                doctor = ahms.search_doctor_by_id(doctor_id)
                if doctor:
                    print("{:>4}  {:<10}  {:<12}  {:<9}  {:<15}  {:<7}".format("id", "name", "specialist", "timing",
                                                                               "qualification", "roomNb"))
                    print("-" * 53)
                    print(
                        "{:>4}  {:<10}  {:<12}  {:<9}  {:<15}  {:<7}".format(doctor.id, doctor.name, doctor.specialist,
                                                                             doctor.timing, doctor.qualification,
                                                                             doctor.room_number))
                else:
                    print("Doctor not Found")
            elif doctor_choice == '3':
                doctor_name = input("Enter the doctor name:\n")
                doctor = ahms.search_doctor_by_name(doctor_name)
                if doctor:
                    print("{:>4}  {:<10}  {:<12}  {:<9}  {:<15}  {:<7}".format("id", "name", "specialist", "timing",
                                                                               "qualification", "roomNb"))
                    print("-" * 53)
                    print(
                        "{:>4}  {:<10}  {:<12}  {:<9}  {:<15}  {:<7}".format(doctor.id, doctor.name, doctor.specialist,
                                                                             doctor.timing, doctor.qualification,
                                                                             doctor.room_number))
                else:
                    print("Doctor not Found")
            elif doctor_choice == '4':
                id = int(input("Enter the doctor ID:\n"))
                name = input("Enter the doctor name:\n")
                specialist = input("Enter the doctor specialist:\n")
                timing = input("Enter the doctor timing:\n")
                qualification = input("Enter the doctor qualification:\n")
                room_number = int(input("Enter the doctor room number:\n"))
                ahms.add_doctor(id, name, specialist, timing, qualification, room_number)
            elif doctor_choice == '5':
                id = int(input("Enter the doctor ID:\n"))
                name = input("Enter the doctor name:\n")
                specialist = input("Enter the doctor specialist:\n")
                timing = input("Enter the doctor timing:\n")
                qualification = input("Enter the doctor qualification:\n")
                room_number = int(input("Enter the doctor room number:\n"))
                ahms.edit_doctor_info(id, name, specialist, timing, qualification, room_number)
            elif doctor_choice == '6':
                break
            else:
                print("Error: Invalid choice. Please select a valid option.")

    elif choice == '2':
        # Facilities menu loop
        while True:
            print("\nFacilities Menu:")
            print("1 - Display Facilities list\n2 - Add facility\n3 - Back to the Main Menu")
            facility_choice = input()

            # Handle facility menu choice
            if facility_choice == '1':
                ahms.display_facilities()
            elif facility_choice == '2':
                name = input("Enter the facility name:\n")
                ahms.add_facility(name)
            elif facility_choice == '3':
                break
            else:
                print("Error: Invalid choice. Please select a valid option.")

    elif choice == '3':
        # Laboratories menu loop
        while True:
            print("\nLaboratories Menu:")
            print("1 - Display Laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu")
            lab_choice = input()

            # Handle laboratory menu choice
            if lab_choice == '1':
                ahms.display_laboratories()
            elif lab_choice == '2':
                facility = input("Enter the laboratory facility:\n")
                cost = int(input("Enter the laboratory cost:\n"))
                ahms.add_laboratory(facility, cost)
            elif lab_choice == '3':
                break
            else:
                print("Error: Invalid choice. Please select a valid option.")

    elif choice == '4':
        # Patients menu loop
        while True:
            print("\nPatients Menu:")
            print("1 - Display Patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit Patient info\n5 - Back to the Main Menu")
            patient_choice = input()

            # Handle patient menu choice
            if patient_choice == '1':
                ahms.display_patients()
            elif patient_choice == '2':
                patient_id = int(input("Enter the patient ID:\n"))
                patient = ahms.search_patient_by_id(patient_id)
                if patient:
                    print("{:<4}  {:<20}  {:<15}  {:<10}  {:<6}".format("ID", "Name", "Disease", "Gender", "Age"))
                    print("-" * 60)
                    print("{:<4}  {:<20}  {:<15}  {:<10}  {:<6}".format(patient.id, patient.name, patient.disease,
                                                                        patient.gender, patient.age))
                else:
                    print("Patient not found")
            elif patient_choice == '3':
                id = int(input("Enter the patient ID:\n"))
                name = input("Enter the patient name:\n")
                disease = input("Enter the patient disease:\n")
                gender = input("Enter the patient gender:\n")
                age = int(input("Enter the patient age:\n"))
                ahms.add_patient(id, name, disease, gender, age)
            elif patient_choice == '4':
                # Edit Patient info
                patient_id = int(input("Enter the patient ID:\n"))
                patient = ahms.search_patient_by_id(patient_id)
                if patient:
                    name = input("Enter the patient name:\n")
                    disease = input("Enter the patient disease:\n")
                    gender = input("Enter the patient gender:\n")
                    age = int(input("Enter the patient age:\n"))
                    ahms.edit_patient_info(patient_id, name, disease, gender, age)
                else:
                    print("Patient not found")
            elif patient_choice == '5':
                break
            else:
                print("Error: Invalid choice. Please select a valid option.")

    elif choice == '0':
        print("Exiting the Alberta Hospital (AH) Management system. Goodbye!")
        break
    else:
        print("Error: Invalid choice. Please select a valid option.")





