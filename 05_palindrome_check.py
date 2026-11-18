"""
Program 5: Palindrome Check
Aim: To check whether a given string or number is a palindrome.
"""


def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def main():
    text = input("Enter a string or number: ")
    if is_palindrome(text):
        print(f'"{text}" is a palindrome')
    else:
        print(f'"{text}" is not a palindrome')


if __name__ == "__main__":
    main()
