def FindElement(A, n):
    # traverse array elements
    for i in range(0, n, 1):
        # If we found that such number
        flag = 0
        # check All the elements on its
        # left are smaller
        for j in range(0, i, 1):
            if (A[j] >= A[i]):
                flag = 1
                break
        # check All the elements on its
        # right are Greater
        for j in range(i + 1, n, 1):
            if (A[j] <= A[i]):
                flag = 1
                break
        # If flag == 0 indicates we found
        # that number
        if (flag == 0):
            return A[i]
    return -1
n = int(input("Enter length: "))
arr = []
for i in range(n):
    d = int(input("Enter element : "))
    arr.append(d)
print("Element is: ", FindElement(arr, n))

# This code is contributed by Tanmay Goel.
