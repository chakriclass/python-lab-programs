"""
Program 2: Fibonacci Series
Aim: To print the first N terms of the Fibonacci series.
"""


def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def main():
    n = int(input("Enter the number of terms: "))
    if n <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci series:", *fibonacci(n))


if __name__ == "__main__":
    main()
