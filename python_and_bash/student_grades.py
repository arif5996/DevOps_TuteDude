# Dictionary to store students and grades
students = {}

def add_student():
    name = input("Enter student name: ")
    grade = input("Enter grade: ")

    if name in students:
        print("Student already exists.")
    else:
        students[name] = grade
        print("Student added successfully.")

def update_grade():
    name = input("Enter student name: ")

    if name in students:
        grade = input("Enter new grade: ")
        students[name] = grade
        print("Grade updated successfully.")
    else:
        print("Student not found.")

def print_grades():
    if students:
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")
    else:
        print("No student records found.")

def main():
    while True:
        print("\n1. Add Student")
        print("2. Update Grade")
        print("3. Print Grades")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_grade()
        elif choice == "3":
            print_grades()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
  main()