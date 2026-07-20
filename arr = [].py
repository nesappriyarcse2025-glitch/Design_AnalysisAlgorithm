arr = []

print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)

print("\n1. Ascending Order")
print("2. Descending Order")
choice = int(input("Enter your choice (1 or 2): "))
if choice == 1:
    arr.sort()
    print("\nNumbers in Ascending Order:")
    print(arr)

elif choice == 2:
    arr.sort(reverse=True)
    print("\nNumbers in Descending Order:")
    print(arr)

else:
    print("Invalid Choice!")