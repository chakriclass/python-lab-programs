"""
Program 1: Simple Calculator
Aim: To perform basic arithmetic operations using functions.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def main():
    print("Simple Calculator")
    print("1. Add  2. Subtract  3. Multiply  4. Divide")
    choice = input("Enter choice (1-4): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    operations = {"1": add, "2": subtract, "3": multiply, "4": divide}
    if choice in operations:
        print("Result:", operations[choice](a, b))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
