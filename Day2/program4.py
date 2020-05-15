n = int(input("Input size: "))
for i in range(1, n):
    print("*" * (n - i) + "  " * i + "*" * (n - i))
for j in range(1, n):
    print("*" * j + "  " * (n - j) + "*" * j)
    
# Code by Tanmay Goel
