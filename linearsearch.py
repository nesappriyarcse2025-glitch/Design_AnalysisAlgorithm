# Linear Search in Python

arr = [10, 25, 30, 45, 50, 65, 70]  # 7 elements

key = int(input("Enter the key element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at position", i + 1)
        found = True
        break

if not found:
    print("Element not found")