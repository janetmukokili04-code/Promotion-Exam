# Hospital Management System

patients = {}

# ADD PATIENT 
def add_patient():
    patient_id = input("Enter Patient ID: ")

    if patient_id in patients:
        print("Patient already exists.")
        return

    name = input("Enter Full Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    diagnosis = input("Enter Diagnosis: ")

    treatments = {}

    print("Enter at least 2 treatments")

    for i in range(2):
        t_name = input("Treatment Name: ")
        cost = float(input("Cost: "))

        if cost <= 0:
            print("Cost must be positive.")
            return

        treatments[t_name] = cost

    more = input("Do you want to add more treatments? (yes/no): ")

    while more.lower() == "yes":
        t_name = input("Treatment Name: ")
        cost = float(input("Cost: "))

        if cost <= 0:
            print("Cost must be positive.")
            return

        treatments[t_name] = cost
        more = input("Add another? (yes/no): ")

    patients[patient_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "diagnosis": diagnosis,
        "treatments": treatments
    }

    print("Patient added successfully.")


#  VIEW ALL PATIENTS 
def view_all_patients():
    if len(patients) == 0:
        print("No patients found.")
    else:
        for pid in patients:
            print("ID:", pid,
                  "| Name:", patients[pid]["name"],
                  "| Diagnosis:", patients[pid]["diagnosis"])


#  VIEW PATIENT REPORT 
def view_patient_report():
    pid = input("Enter Patient ID: ")

    if pid not in patients:
        print("Patient not found.")
        return

    patient = patients[pid]

    print("\nPatient Details")
    print("Name:", patient["name"])
    print("Age:", patient["age"])
    print("Gender:", patient["gender"])
    print("Diagnosis:", patient["diagnosis"])

    total = 0
    print("\nTreatments:")
    for t in patient["treatments"]:
        cost = patient["treatments"][t]
        print(t, ":", cost)
        total += cost

    print("Total Bill:", total)


#  UPDATE PATIENT 
def update_patient():
    pid = input("Enter Patient ID: ")

    if pid not in patients:
        print("Patient not found.")
        return

    print("1. Update Diagnosis")
    print("2. Add Treatment")
    print("3. Update Treatment Cost")
    print("4. Remove Treatment")

    choice = input("Choose option: ")

    if choice == "1":
        new_diag = input("Enter new diagnosis: ")
        patients[pid]["diagnosis"] = new_diag
        print("Diagnosis updated.")

    elif choice == "2":
        t_name = input("Treatment Name: ")
        cost = float(input("Cost: "))
        if cost <= 0:
            print("Cost must be positive.")
            return
        patients[pid]["treatments"][t_name] = cost
        print("Treatment added.")

    elif choice == "3":
        t_name = input("Enter treatment name: ")
        if t_name in patients[pid]["treatments"]:
            cost = float(input("New cost: "))
            if cost <= 0:
                print("Cost must be positive.")
                return
            patients[pid]["treatments"][t_name] = cost
            print("Cost updated.")
        else:
            print("Treatment not found.")

    elif choice == "4":
        t_name = input("Enter treatment name to remove: ")
        if t_name in patients[pid]["treatments"]:
            del patients[pid]["treatments"][t_name]
            print("Treatment removed.")
        else:
            print("Treatment not found.")

    else:
        print("Invalid choice.")


#  DELETE PATIENT 
def delete_patient():
    pid = input("Enter Patient ID to delete: ")

    if pid in patients:
        del patients[pid]
        print("Patient deleted.")
    else:
        print("Patient not found.")


#  SEARCH PATIENT 
def search_patient():
    search = input("Enter Patient ID or Name: ")

    found = False

    for pid in patients:
        if search == pid or search.lower() == patients[pid]["name"].lower():
            print("Found:", pid, "-", patients[pid]["name"])
            found = True

    if not found:
        print("Patient not found.")


#  HOSPITAL STATISTICS 
def hospital_statistics():
    if len(patients) == 0:
        print("No records available.")
        return

    total_patients = len(patients)
    total_revenue = 0

    highest = 0
    lowest = None
    highest_name = ""
    lowest_name = ""

    for pid in patients:
        bill = sum(patients[pid]["treatments"].values())
        total_revenue += bill

        if bill > highest:
            highest = bill
            highest_name = patients[pid]["name"]

        if lowest is None or bill < lowest:
            lowest = bill
            lowest_name = patients[pid]["name"]

    print("\nHospital Statistics")
    print("Total Patients:", total_patients)
    print("Total Revenue:", total_revenue)
    print("Highest Bill:", highest_name, "-", highest)
    print("Lowest Bill:", lowest_name, "-", lowest)


#  MAIN MENU 
def main():
    while True:
        print("\n1. Add Patient")
        print("2. View All Patients")
        print("3. View Patient Report")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Search Patient")
        print("7. Hospital Statistics")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_all_patients()
        elif choice == "3":
            view_patient_report()
        elif choice == "4":
            update_patient()
        elif choice == "5":
            delete_patient()
        elif choice == "6":
            search_patient()
        elif choice == "7":
            hospital_statistics()
        elif choice == "8":
            print("Program ended.")
            break
        else:
            print("Invalid choice.")


main()