a=input("Enter string: ")
b=""
for i in range(0,len(a)):
    if a[i]==" ":
        b=b+" "
    elif a[i] not in b:
        b=b+a[i]
print("String after removed duplicates: ",b)

# Code by Tanmay Goel