students = []

def add_student():
    student_id = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")
    students.append({
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Department": department
    })
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
    else:
        print("\n--- Student List ---")
        for s in students:
            print(f"ID: {s['ID']}, Name: {s['Name']}, Age: {s['Age']}, Department: {s['Department']}")

def delete_student():
    student_id = input("Enter ID of student to delete: ")
    for s in students:
        if s['ID'] == student_id:
            students.remove(s)
            print("Student removed successfully!")
            return
    print("Student not found.")

def main():
    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()