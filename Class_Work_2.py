myList = []

while ("True"):
    print("1. Add an Element to the list")
    print("2. Remove an Element from the list")
    print("3. Replace an Element in the list")
    print("4. Sort the Elements in the list")
    print("5. Print the list Elements")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        myList.append(int(input("Enter a number: ")))
        print(myList)
    elif choice == 2:
        myList.remove(int(input("Enter a number: ")))
        print(myList)

    elif choice == 3:
        old_element = int(input("Enter the number you want to replace: "))
        new_element = int(input("Enter the new number: "))

        index = 0
        for i in myList:
            if i == old_element:
                break
            index = index + 1
        myList[index] = new_element
        print(myList)

    elif choice == 4:
        myList.sort()
        print(myList)

    elif choice == 5:
        print("List Elements")
        print(myList)

    elif choice == 6:
        print("Exit")
        break







