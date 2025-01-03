num1 = int(input("Enter The First Number:"))
num2 = int(input("Enter The Second Number:"))

def multiply():
    mul = num1 * num2
    print("The Product Of Numbers:", mul)

def addition():
    add = num1 + num2
    print("The Sum Of Numbers:", add)

choice = int(input("Which Operation You Want: 1.Add 2.Multiply"))

if (choice == 1):
    addition()

if (choice == 2):
    multiply()