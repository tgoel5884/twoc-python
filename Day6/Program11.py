n = int(input("Enter length: "))
arr = []
for i in range(n):
    d = int(input("Enter element : "))
    arr.append(d)
arr.sort()
maxi=arr[n-1]*arr[n-2]*arr[n-3]
print("Maximum Product: ",maxi)


# This code is contributed by Tanmay Goel.
