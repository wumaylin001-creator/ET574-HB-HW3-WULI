students = ["Jon", "Kim", "Lee"]
students.append("Sara")
students.append("Miko")

def greet_students(student_list):
    for student in student_list:
        print(f"Hi {student}")
    print(f"Total students: {len(student_list)}")

greet_students(students)