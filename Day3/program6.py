def findSmallest(arr, n):
    res = 1
    for i in range(0, n):
        if arr[i] <= res:
            res = res + arr[i]
        else:
            break
    return res


n1 = int(input("Enter number of elements in list: "))
arr1 = []
print("Enter elements of list: ")
for i in range(n1):
    c = int(input())
    arr1.append(c)
arr1.sort()
print("Smallest non-representable number: ", findSmallest(arr1, n1))

# Code by Tanmay Goel
