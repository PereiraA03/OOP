a = int(input("Enter the value of A"))
b = int(input("Enter the value of B"))

while ("True"):
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiply")
    print("4 Divide")
    print("5 Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        c = a + b
        print(c)
    elif choice == "2":
        c = a - b
        print(c)
    elif choice == "3":
        c = a * b
        print(c)
    elif choice == "4":
        c = a / b
        print(c)
    elif choice == "5":
        exit()



