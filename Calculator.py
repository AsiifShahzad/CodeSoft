def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero"

while True:
    print("\nSimple Calculator")
    print("Press 1 for Addition\n")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    print("Press 5 for Exit")

    choice = input("Enter your choice\n")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result = ", add(num1, num2))
        elif choice == '2':
            print("Result = ", subtract(num1, num2))
        elif choice == '3':
            print("Result = ", multiply(num1, num2))
        elif choice == '4':
            print("Result = ", divide(num1, num2))
    elif choice == '5':
        print("Exiting the calculator\n")
        break
    else:
        print("Invalid choice\n")

