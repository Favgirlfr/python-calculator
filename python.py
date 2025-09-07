# Simple calculator

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

operation = input("Enter an operation (+, -, *, /): ")

try:
    if operation == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter +, -, *, or /.")
except Exception as e:
    print(f"An error occurred: {e}")
