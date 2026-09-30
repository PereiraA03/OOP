class Student:
    def _init_(self):
        self.id = ""
        self.name = ""
        self.department = ""

    def create_new_student(self):
        self.id = input("Enter student ID: ")
        self.name = input("Enter name: ")
        self.department = input("Enter student Dept: ")

    def display_student(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)

Stu = Student ()

Stu.create_new_student()
Stu.display_student()

myStudents = []

Stu = Student ()
Stu.create_new_student()
Stu.display_student()

myStudents.append(Stu)
Stu = Student ()
Stu.create_new_student()
Stu.display_student()
myStudents.append(Stu)

print(myStudents)