# Dictionary

myEmployees = {}

def add_Employee():
    name = input("Enter employee's name: ")
    basicPay = int(input("Enter basic pay: "))
    allowance = int(input("Enter allowance: "))
    deductions = int(input("Enter deduction: "))
    taxes = int(input("Enter taxes: "))

    grossPay = basicPay + allowance
    netPay = grossPay - deductions - taxes

    myEmployees.update({
        name: {
            "Basic Pay": basicPay,
            "Allowance": allowance,
            "Deductions": deductions,
            "Taxes": taxes,
            "Gross Pay": grossPay,
            "Net Pay": netPay
        }
    })
    print("Employee added")

def delete_Employee():
    name = input("Enter employee name to delete: ")

    if name in myEmployees:
        del myEmployees[name]
        print("Employee deleted.")
    else:
        print("Employee not found.")

def modify_Employee():
    name = input("Enter employee's name to modify: ")

    if name in myEmployees:
        basicPay = int(input("Enter new basic pay: "))
        allowance = int(input("Enter new allowance: "))
        deductions = int(input("Enter new deductions: "))
        taxes = int(input("Enter new taxes: "))

    grossPay = basicPay + allowance
    netPay = grossPay - deductions - taxes

    myEmployees.update({
        name: {
            "Basic Pay": basicPay,
            "Allowance": allowance,
            "Deductions": deductions,
            "Taxes": taxes,
            "Gross Pay": grossPay,
            "Net Pay": netPay
        }
    })
    print("Employee modified")

def display_Employees():

    for name in myEmployees:
        print("Employee Name:", name)
        print("Basic Pay:", myEmployees[name]["Basic Pay"])
        print("Allowance:", myEmployees[name]["Allowance"])
        print("Deductions:", myEmployees[name]["Deductions"])
        print("Taxes:", myEmployees[name]["Taxes"])
        print("Gross Pay:", myEmployees[name]["Gross Pay"])
        print("Net Pay:", myEmployees[name]["Net Pay"])
        print()

# Main Menu

while True:

    print()
    print("EMPLOYEE PAYROLL MENU")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Modify Employee")
    print("4. Display Employees")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_Employee()

    elif choice == "2":
        delete_Employee()

    elif choice == "3":
        modify_Employee()

    elif choice == "4":
        display_Employees()

    elif choice == "5":
        print("Exit")
        break

    else:
        print("Invalid choice")