n = int(input("Input size: "))
for i in range(n, 0, -1):
    for j in range(0, i):
        if j == i - 1:
            print(i)
        else:
            print(i, "*", end=" ")
for i in range(1, n + 1):
    for j in range(0, i):
        if j == i - 1:
            print(i)
        else:
            print(i, "*", end=" ")


# Code by Tanmay Goel
