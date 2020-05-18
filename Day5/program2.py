n = int(input("Enter size of array: "))
a = []
for i in range (n):
    b = input("Enter element: ")
    a.append(b)
for i in range(0,n-1):
    a[i]=max(a[i+1:])
print("Resultant: ",a)

# Code by Tanmay Goel