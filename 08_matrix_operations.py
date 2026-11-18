"""
Program 8: Matrix Addition and Multiplication
Aim: To perform addition and multiplication of two matrices.
"""


def read_matrix(name):
    rows = int(input(f"Enter number of rows in {name}: "))
    cols = int(input(f"Enter number of columns in {name}: "))
    print(f"Enter {name} row by row (values separated by spaces):")
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row[:cols])
    return matrix


def add_matrices(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def multiply_matrices(a, b):
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def main():
    a = read_matrix("Matrix A")
    b = read_matrix("Matrix B")

    if len(a) == len(b) and len(a[0]) == len(b[0]):
        print("Sum of matrices:")
        print_matrix(add_matrices(a, b))
    else:
        print("Addition not possible: matrices must have the same size")

    if len(a[0]) == len(b):
        print("Product of matrices:")
        print_matrix(multiply_matrices(a, b))
    else:
        print("Multiplication not possible: columns of A must equal rows of B")


if __name__ == "__main__":
    main()
