
number1 = int(input("Enter number1"))
number2 = int(input("Enter number2"))
number3 = int(input("Enter number3"))

#Find the biggest of the three numbers
#Find the smallest of the three numbers

if number1 > number2 and number1 > number3:
    print("number1 is the biggest")
if number2 > number1 and number2 > number3:
    print("number2 is the biggest")
if number3 > number1 and number3 > number2:
    print("number3 is the biggest")


if number1 < number2 and number1 < number3:
    print("number1 is the smallest")
if number2 < number1 and number2 < number3:
    print("number2 is the smallest")
if number3 < number1 and number3 < number2:
    print("number3 is the smallest")