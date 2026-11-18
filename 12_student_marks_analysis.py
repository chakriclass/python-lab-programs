"""
Program 12: Student Marks Analysis using Pandas and Matplotlib
Aim: To analyse student marks and visualise the results with a bar chart.
Requirements: pip install pandas matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt


def main():
    data = {
        "Name": ["Arun", "Divya", "Karthik", "Meena", "Rahul", "Sneha"],
        "Python": [85, 92, 78, 88, 64, 95],
        "Java": [80, 89, 72, 91, 70, 87],
        "C": [75, 94, 69, 85, 68, 90],
    }
    df = pd.DataFrame(data)
    df["Average"] = df[["Python", "Java", "C"]].mean(axis=1).round(2)

    print("Student Marks:")
    print(df.to_string(index=False))
    print("\nSubject-wise class average:")
    print(df[["Python", "Java", "C"]].mean().round(2).to_string())
    topper = df.loc[df["Average"].idxmax()]
    print(f"\nTopper: {topper['Name']} with average {topper['Average']}")

    df.plot(x="Name", y=["Python", "Java", "C"], kind="bar", figsize=(8, 5))
    plt.title("Subject-wise Marks of Students")
    plt.ylabel("Marks")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("marks_chart.png")
    print("\nChart saved as marks_chart.png")


if __name__ == "__main__":
    main()
