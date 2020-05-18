a = int(input("Enter the no of tuples you want to add in the list: "))
b = int(input("Enter the no of elements you want to add in each tuple: "))
List = []
for i in range(a):
    print("Enter the elements in Tuple", i + 1)
    Tuple = []
    for j in range(b):
        Tuple.append(int(input("Enter the element: ")))
    List.append(tuple(Tuple))
N = int(input("Enter index about which you want to sort the list: "))
List.sort(key = lambda x : x[N])
print("After sorting tuple List by Nth index sort:",List)


# Code by Tanmay Goel
