"""
Program 3: Prime Numbers in a Range
Aim: To find all prime numbers between two given numbers.
"""


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def main():
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    if primes:
        print(f"Prime numbers between {start} and {end}:", *primes)
    else:
        print("No prime numbers in this range")


if __name__ == "__main__":
    main()
