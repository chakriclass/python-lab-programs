"""
Program 7: Sorting Algorithms
Aim: To sort a list using Bubble Sort, Selection Sort and Insertion Sort.
"""


def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def main():
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Bubble Sort   :", bubble_sort(arr))
    print("Selection Sort:", selection_sort(arr))
    print("Insertion Sort:", insertion_sort(arr))


if __name__ == "__main__":
    main()
