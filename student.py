students = []

def register_student(name, student_id):
    student = {
        "id": student_id,
        "name": name
    }

    students.append(student)
    print("Student registered successfully.")