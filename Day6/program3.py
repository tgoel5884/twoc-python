flag=1
n = int(input("Enter length: "))
arr = []
for i in range(n):
    d = int(input("Enter element : "))
    arr.append(d)
for i in range(n):
    if flag in arr:
        flag+=1
    else:
        break
print("Smallest missing number: ",flag)


# This code is contributed by Tanmay Goel.
