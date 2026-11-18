"""
Program 9: File Handling - Word Count
Aim: To count lines, words and characters in a text file and find the most frequent word.
"""

from collections import Counter


def analyse_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    lines = content.splitlines()
    words = content.lower().split()
    return len(lines), len(words), len(content), Counter(words).most_common(1)


def main():
    filename = input("Enter file name (e.g. sample.txt): ")
    try:
        lines, words, chars, common = analyse_file(filename)
        print("Lines     :", lines)
        print("Words     :", words)
        print("Characters:", chars)
        if common:
            print(f"Most frequent word: '{common[0][0]}' ({common[0][1]} times)")
    except FileNotFoundError:
        print("Error: File not found")


if __name__ == "__main__":
    main()
