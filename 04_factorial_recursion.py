"""
Program 4: Factorial using Recursion
Aim: To find the factorial of a number using a recursive function.
"""


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def main():
    n = int(input("Enter a number: "))
    if n < 0:
        print("Factorial is not defined for negative numbers")
    else:
        print(f"Factorial of {n} is {factorial(n)}")


if __name__ == "__main__":
    main()
