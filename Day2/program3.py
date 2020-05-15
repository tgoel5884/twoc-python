N = int(input("Enter Size: "))

for i in range(N):
    for j in range(N):
        if (i == j) or ((N - j -1) == i):
            print('*', end = '')
        else:
            print(' ', end = '')
    print('')

# Code by Tanmay Goel