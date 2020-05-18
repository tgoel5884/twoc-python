a = dict()
b = dict()
n = int(input("Enter size of dictionary: "))
for i in range(n):
    k = input("Enter key: ")
    l = input("Enter value: ")
    a[k] = l
for key, value in a.items():
    if value not in b.values():
        b[key] = value
print("Edited dictionary: ", b)

# Code by Tanmay Goel