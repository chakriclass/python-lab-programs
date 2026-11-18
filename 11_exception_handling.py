"""
Program 11: Exception Handling
Aim: To handle runtime errors using try, except, else and finally,
     and to raise a user-defined exception.
"""


class InvalidAgeError(Exception):
    """Raised when the entered age is not valid for voting."""


def check_voting_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above to vote")
    return "Eligible to vote"


def main():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
    except ValueError:
        print("Error: Please enter integers only")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    else:
        print("Result:", result)
    finally:
        print("Division block completed")

    try:
        age = int(input("Enter your age: "))
        print(check_voting_age(age))
    except InvalidAgeError as error:
        print("Custom Exception:", error)
    except ValueError:
        print("Error: Please enter a valid age")


if __name__ == "__main__":
    main()
