n = int(input("Enter the no of votes: "))
a = []
for i in range(n):
    a.append(input("Enter name: "))
b = []
for name in a:
    b.append((name, a.count(name)))
b.sort(key=lambda x: x[0], reverse=True)
b.sort(key=lambda x: x[1])
print("Candidate who won the election: ", b[-1][0])

# Code by Tanmay Goel
