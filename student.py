# Student Record System using Python

students = {}

# Add Student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    students[roll] = {
        "Name": name,
        "Marks": marks
    }

    print("Student record added successfully!\n")


# Display All Students
def display_students():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        print("\n----- Student Records -----")
        for roll, details in students.items():
            print("Roll Number :", roll)
            print("Name        :", details["Name"])
            print("Marks       :", details["Marks"])
            print("----------------------------")


# Search Student
def search_student():
    roll = input("Enter Roll Number to search: ")

    if roll in students:
        print("\nStudent Found")
        print("Name  :", students[roll]["Name"])
        print("Marks :", students[roll]["Marks"])
    else:
        print("Student record not found.\n")


# Update Student Record
def update_student():
    roll = input("Enter Roll Number to update: ")

    if roll in students:
        name = input("Enter New Name: ")
        marks = int(input("Enter New Marks: "))

        students[roll]["Name"] = name
        students[roll]["Marks"] = marks

        print("Record updated successfully!\n")
    else:
        print("Student record not found.\n")


# Delete Student Record
def delete_student():
    roll = input("Enter Roll Number to delete: ")

    if roll in students:
        del students[roll]
        print("Record deleted successfully!\n")
    else:
        print("Student record not found.\n")


# Main Menu
while True:
    print("\n====== Student Record System ======")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Program Ended.")
        break

    else:
        print("Invalid choice! Please try again.")