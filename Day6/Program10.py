k = int(input("Enter number of lists: "))
n = int(input("Enter number of elements in each list: "))
a=[]
for i in range(k):
    m=[]
    for j in range(n):
        m.append(int(input("Enter element: ")))
    a.append(m)
print("Lists: ",a)
k=[]
for i in range(len(a)):
    for j in range(len(a[i])):
        k.append(a[i][j])
k.sort()
print("Sorted list: ",k)

# This code is contributed by Tanmay Goel
