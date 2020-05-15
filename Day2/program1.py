print("Enter number to check for Even-Odd, Prime, Palindrome, Armstrong: ")
a = int(input())
b = a

# For Even-Odd
if a % 2 == 0:
    print(a, "is Even")
else:
    print(a, "is Odd")

# For Prime
c = 0
for i in range(1, a + 1):
    if a % i == 0:
        c = c+1
if c == 2:
    print(a, "is Prime")
else:
    print(a, "is not Prime")

# For Palindrome
rev = 0
while b != 0:
    rem = b % 10
    rev = rev * 10 + rem
    b = b // 10
if rev == a:
    print(a, "is Palindrome")
else:
    print(a, "is not Palindrome")

# For Armstrong
e = a
sum = 0
while e != 0:
    rem2 = e % 10
    sum = sum + (rem2 * rem2 * rem2)
    e = e // 10
if sum == a:
    print(a, "is Armstrong number")
else:
    print(a, "is not Armstrong number")





# Code by Tanmay Goel