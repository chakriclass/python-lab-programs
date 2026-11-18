"""
Program 6: Linear Search and Binary Search
Aim: To search for an element in a list using linear and binary search.
"""


def linear_search(arr, key):
    for index, value in enumerate(arr):
        if value == key:
            return index
    return -1


def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    key = int(input("Enter element to search: "))

    pos = linear_search(arr, key)
    print("Linear Search:", f"found at index {pos}" if pos != -1 else "not found")

    sorted_arr = sorted(arr)
    print("Sorted list for Binary Search:", sorted_arr)
    pos = binary_search(sorted_arr, key)
    print("Binary Search:", f"found at index {pos}" if pos != -1 else "not found")


if __name__ == "__main__":
    main()
