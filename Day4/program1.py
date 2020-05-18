a=[]
n=int(input("Enter number of elements of tuple: "))
print("Enter elements of tuple: ")
for i in range(n):
    b=input()
    a.append(b)
tuple(a)
d=input("Enter element whose occurrence you want to know: ")
print(d,"occurs",a.count(d),"times")

# Code by Tanmay Goel
