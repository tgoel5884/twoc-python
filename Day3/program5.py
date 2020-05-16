a=[]
b=[]
c=[]
d=int(input("Enter number of items in list1: "))
e=int(input("Enter number of items in list2: "))
print("Enter items of list1: ")
for i in range(d):
    f=input()
    a.append(f)
print("Enter items of list2: ")
for j in range(e):
    g=input()
    b.append(g)
print("Intersection: ")
for i in range(d):
    if a[i] not in c:
        c.append(a[i])
for j in range(e):
    if b[j] not in c:
        c.append(b[j])
print(c)

# Code by Tanmay Goel