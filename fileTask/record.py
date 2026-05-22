import json
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def to_dict(self):
        return {
            'name': self.name,
            'roll': self.roll,
            'marks': self.marks
        }

class Studentlist:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.roll] = student

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([student.to_dict() for student in self.students.values()], f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.students = {student.roll: student for student in [Student(**student_data) for student_data in data]}
    def search_student(self, roll):
        return self.students.get(roll, None)
    def delete_student(self, roll):
        if roll in self.students:
            del self.students[roll]

fileName = 'students.json'   
option = -1
student_list = Studentlist()
student_list.load_from_file(fileName)

print("Welcome to the Student Record Management System")
while True:
    print("1. Add student")
    print("2. Save student data to file")
    print("3. Load data from file")
    print("4. Search student")
    print("5. Delete student")
    print("0. Exit")

    option = input("Enter your choice: ")
    if option.isnumeric():
        option = int(option)
    else:
        print("Invalid choice.")
        continue
    if option == 0:
        break

    match option:
        case 1:
            name = input("Enter student name: ")
            roll = input("Enter student roll number: ")
            marks = input("Enter student marks: ")
            student = Student(name, roll, marks)
            student_list.add_student(student)
        case 2:
            student_list.save_to_file(fileName)
        case 3:
            student_list.load_from_file(fileName)
        case 4:
            roll = input("Enter student roll number to search: ")
            student = student_list.search_student(roll)
            if student:
                print(f"Name: {student.name}, Roll: {student.roll}, Marks: {student.marks}")
            else:
                print("Student not found.")
        case 5:
            roll = input("Enter student roll number to delete: ")
            student_list.delete_student(roll)
            print("Student deleted (if it existed)")
        case _:
            print("Invalid choice.")
    
    input("Press Enter to continue...")