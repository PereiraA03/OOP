myStudents={}

def add_student ():
    stu_name = input("Enter student's name: ")
    Lab1 = int(input("Enter grade for Lab 1: "))
    Lab2 = int(input("Enter grade for Lab 2: "))
    Lab3 = int(input("Enter grade for Lab 3: "))
    Lab4 = int(input("Enter grade for Lab 4: "))
    Lab5 = int(input("Enter grade for Lab 5: "))
    Total = Lab1 + Lab2 + Lab3 + Lab4 + Lab5
    Average = Total / 5
    Percentage = (Total / 50) * 100

    myStudents.update({"student1":{"name":stu_name,"Lab 1":Lab1,"Lab 2": Lab2, "Lab 3": Lab3, "Lab 4":Lab4, "Lab 5":Lab5, "Total": Total, "Average": Average, "Percentage": Percentage}})

def delete_student():
    del myStudents [input("Enter Student Number: ")]

add_student()
print(myStudents)

delete_student()
print(myStudents)

