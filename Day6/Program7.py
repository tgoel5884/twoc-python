def A(m, n, s ="% s"):
	print(s % ("A(% d, % d)" % (m, n)))
	if m == 0:
		return n + 1
	if n == 0:
		return A(m - 1, 1, s)
	n2 = A(m, n - 1, s % ("A(% d, %% s)" % (m - 1)))
	return A(m - 1, n2, s)

m=int(input("Enter value of first number: "))
n=int(input("Enter value of second number: "))
print(A(m, n))

# This code is contributed by Tanmay Goel
