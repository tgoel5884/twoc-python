a=[]
b=[]
res=[]
c=int(input("Enter number of elements in dictionary: "))
for i in range(c):
    d=input("Enter element: ")
    a.append(b)
e=int(input("Enter number of elements in array: "))
for i in range(e):
    f=input("Enter element: ")
    b.append(f)
for word in a:
    if set(word).issubset(set(b)):
        res.append(word)
print(res)

# Code by Tanmay Goel