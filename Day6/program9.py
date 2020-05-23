n = int(input("Enter length: "))
arr = []
for i in range(n):
    d = int(input("Enter element : "))
    arr.append(d)
k=int(input("Enter value of k: "))
arr.sort()
print("kth smallest number: ",arr[k-1])


# This code is contributed by Tanmay Goel.
