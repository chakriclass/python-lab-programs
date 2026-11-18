"""
Program 10: Classes and Objects
Aim: To create a Student class and calculate total, average and grade.
"""


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return self.total() / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "O"
        elif avg >= 80:
            return "A+"
        elif avg >= 70:
            return "A"
        elif avg >= 60:
            return "B+"
        elif avg >= 50:
            return "B"
        return "RA"

    def display(self):
        print(f"Name   : {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Total  : {self.total()}")
        print(f"Average: {self.average():.2f}")
        print(f"Grade  : {self.grade()}")


def main():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = list(map(float, input("Enter marks separated by spaces: ").split()))
    if not marks:
        print("Please enter at least one mark")
        return
    Student(name, roll_no, marks).display()


if __name__ == "__main__":
    main()
