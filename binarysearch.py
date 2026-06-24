# Binary Search in Python

arr = [10, 20, 30, 40, 50, 60, 70]  # Sorted array with 7 elements

key = int(input("Enter the key element to search: "))

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at position", mid + 1)
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")