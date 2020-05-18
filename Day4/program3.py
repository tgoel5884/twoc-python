a = dict()
n = int(input("Enter size of dictionary: "))
for i in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    a[k] = v
print("Second largest value: ", list(sorted(a.values()))[-2])

# Code by Tanmay Goel