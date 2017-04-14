def LCS(X, Y):
	m = len(X)
	n = len(Y)
	c = [[0 for i in range(n + 1)] for j in range(m + 1)]
	b = [[(j, i) for i in range(n + 1)] for j in range(m + 1)]

	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if X[i - 1] == Y[j - 1]:
				c[i][j] = c[i - 1][j - 1] + 1
				b[i][j] = (i - 1, j - 1)
			else:
				temp = max((c[i - 1][j], (i - 1, j)), (c[i][j - 1], (i, j - 1)))
				c[i][j] = temp[0]
				b[i][j] = temp[1]

	col, row = m, n
	route = []
	while col != 0 and row != 0:
		temp0, temp1 = col, row
		col, row = b[col][row]
		if col == temp0 - 1 and row == temp1 - 1:
			route.append(X[temp0 - 1])

	return c[m][n], route[::-1]

X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'A']
print LCS(X, Y)