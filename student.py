students = []

def add_student(name):
    students.append(name)
    print("Student registered successfully.")

def display_students():
    print("\n===== Students =====")

    if not students:
        print("No students registered.")
    else:
        for student in students:
            print("-", student)