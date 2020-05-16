a=[]
c=[]
b=int(input("Enter number of items to be in list: "))
print("Enter items: ")
for i in range(b):
    d=input()
    a.append(d)
for j in range(len(a)):
    if a[j] not in c:
        c.append(a[j])
print("List after removed duplicate items: ",c)

# Code by Tanmay Goel
