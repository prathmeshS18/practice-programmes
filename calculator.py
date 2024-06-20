

def add(x , y):
    return x + y

def substract(x , y):
    return x- y

def multiply(x , y):
    return x * y

def devide(x , y):
    return x / y

print("select operation")
print("1.add")
print("2.substract")
print("3.multiplication")
print("4.division")

while True:
    choice = input("Enter choice(1/2/3/4):")

    if choice in ("1","2","3","4"):
        x = int(input("Enter the 1st no:"))
        y = int(input("Enter the 2nd no:"))
    
    if choice == '1':
        print(x+y)

    if choice == '2':
       print(x-y)

    elif choice == '3':
       print(x*y)

    elif  choice == '4':
       print(x/y)
    
    z = next_calculation=input("want to do next calculation?(yes/no)")
    if next_calculation == "yes":
        continue
    elif next_calculation == "no":
        break

    else:
      print(" invalid input")

    

