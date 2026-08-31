number1 = int(input("enter number1"))
operator = input("enter operator")
number2 = int(input("enter number2"))

if operator == "+":
   c= number1 + number2
print("The sum of the numbers is", c)

elif operator == "-":
    c= number1 - number2
    print("The difference of the numbers is", c)

elif operator == "*":
c= number1 * number2
print("The product of the numbers is", c)

elif operator == "/":
c= number1 / number2
print("The quotient of the numbers is", c)