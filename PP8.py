mylist = [2,56,43,18,29,9]

mylist.append(66)         #Add element to the list (value)
print(mylist)

mylist.remove(56)       #remove an element (value)
print(mylist)

mylist.pop()        #removes the last element in the list (index)
print(mylist)

mylist.sort()          #sort in ascending order
print(mylist)

newlist = mylist.copy()   #copies list and changes name
newlist.append (1001)
print(newlist)          #new list and keep the last list the same

newvalue = int(input("Enter a number: "))
if newvalue in mylist:
    print("Element is in the list")
else:
    print("Element not found")
