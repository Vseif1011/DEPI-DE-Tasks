class Hospital: 
    currentStaffCounter = 0
    def __init__(self,name,location):
        self.name = name 
        self.location = location
        self.doctors = []
        self.patients = []
    def addDoctor(self,doctor):
        self.doctors.append(doctor)
    def addPatient(self,patient):
        self.patients.append(patient)
    def showDoctors(self):
        for i in range(len(self.doctors)): 
            print(f"{i+1}- {self.doctors[i].name} ")
    def showPatients(self):
        for i in range(len(self.patients)): 
            print(f"{i+1}- {self.patients[i].name} ")

class staff: 
    def __init__ (self,name,address,number,age):
        self.name = name
        self.address = address
        self.number = number
        self.age = age
    def showStaffDetails(self):
        print(f"Name: {self.name} | Age: {self.age} | Address: {self.address} | Phone Number : {self.number}")

class Doctor(staff):
    def __init__(self,name,address,number,age,speciality):
        super().__init__(name,address,number,age)
        self.speciality = speciality 
        self.assignedPatientsList = []
        self.uid = Hospital.currentStaffCounter
        Hospital.currentStaffCounter += 1
    def assignPatient(self,patient): 
        self.assignedPatientsList.append(patient)
    def showPatients(self):
        for i in range(len(self.assignedPatientsList)):
            print(f"Patient {i+1} - Name: {self.assignedPatientsList[i].name}")

class Patient(staff):
    def __init__(self,name,address,number,age,illness):
        super().__init__(self,name,address,number,age)
        self.illness = illness
        self.assignedDoctor = None
        self.uid = Hospital.currentStaffCounter
        Hospital.currentStaffCounter += 1
    def assignDoctor(self,doctor):
        self.assignedDoctor = doctor 
    def showInfo(self):
        print(f"Patient name: {self.name} | Patient Age: {self.age} | Patient Ilness: {self.illness}")
        print(f"Assigned Doctor: {self.assignedDoctor.name}")



if __name__ == "__main__":

    hospital = Hospital("City Care Hospital", "Downtown")

    while True:
        print("    Hospital Management System    ")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Assign Doctor to Patient")
        print("4. Show All Doctors")
        print("5. Show All Patients")
        print("6. Show a Doctor's Assigned Patients")
        print("7. Show Patient Info")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Doctor name: ")
            address = input("Address: ")
            number = input("Phone number: ")
            age = input("Age: ")
            speciality = input("Speciality: ")
            doctor = Doctor(name, address, number, age, speciality)
            hospital.addDoctor(doctor)
            print(f"Doctor {name} added successfully.")

        elif choice == "2":
            name = input("Patient name: ")
            address = input("Address: ")
            number = input("Phone number: ")
            age = input("Age: ")
            illness = input("Illness: ")
            patient = Patient(name, address, number, age, illness)
            hospital.addPatient(patient)
            print(f"Patient {name} added successfully.")

        elif choice == "3":
            hospital.showDoctors()
            d_index = int(input("Choose doctor number: ")) - 1
            hospital.showPatients()
            p_index = int(input("Choose patient number: ")) - 1

            doctor = hospital.doctors[d_index]
            patient = hospital.patients[p_index]

            doctor.assignPatient(patient)
            patient.assignDoctor(doctor)
            print(f"Dr. {doctor.name} assigned to patient {patient.name}.")

        elif choice == "4":
            hospital.showDoctors()

        elif choice == "5":
            hospital.showPatients()

        elif choice == "6":
            hospital.showDoctors()
            d_index = int(input("Choose doctor number: ")) - 1
            hospital.doctors[d_index].showPatients()

        elif choice == "7":
            hospital.showPatients()
            p_index = int(input("Choose patient number: ")) - 1
            hospital.patients[p_index].showInfo()

        elif choice == "8":
            break

        else:
            print("Invalid choice, try again.")