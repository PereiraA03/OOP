while ("1"):
    print("1 Area of Rectangle")
    print("2 Volume of Cube")
    print("3 Area of Circle")
    print("4 Circumference of Circle")
    print("5 exit:")

    choice = input("Enter your choice:")

    if choice == "1":
        lenght = int(input("Enter the length of the rectangle:"))
        widht = int(input("Enter the width of the rectangle:"))
        area = lenght * widht
        print(area)

    elif choice == "2":
        lenght = int(input("Enter the length of the cube:"))
        width = int(input("Enter the width of the cube:"))
        height = int(input("Enter the height of the cube:"))
        volume = lenght * width * height
        print(volume)

    elif choice == "3":
        radius = int(input("Enter the radius of the circle:"))
        area_of_circle = 3.14 * radius * radius
        print(area_of_circle)

    elif choice == "4":
        radius = int(input("Enter the radius of the circle:"))
        circum_of_circle = 2 * 3.14 * radius
        print(circum_of_circle)

    elif choice == "5":
        exit()
