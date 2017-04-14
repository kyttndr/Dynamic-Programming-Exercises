def knapsack(W, E):
	n = len(E)
	B = [[0 for i in range(n + 1)] for j in range(W + 1)]
	track = [[(-1, -1) for i in range(n + 1)] for j in range(W + 1)]
	for i in range(1, n + 1):
		for j in range(1, W + 1):
			if E[i - 1][0] <= j:
				if B[j][i - 1] < E[i - 1][1] + B[j - E[i - 1][0]][i - 1]:
					B[j][i] = E[i - 1][1] + B[j - E[i - 1][0]][i - 1]
					track[j][i] = (j - E[i - 1][0], i - 1)
				else:
					B[j][i] = B[j][i - 1]
					track[j][i] = (j, i - 1)
			else:
				B[j][i] = B[j][i - 1]
				track[j][i] = (j, i - 1)

	col, row = W, n
	route = []
	while row != 0 and col != 0:
		temp0, temp1 = col, row
		col, row = track[col][row]
		if col != temp0:
			route.append(E[temp1 - 1])

	return B[W][n], route[::-1]

Elements = [(2, 3), (3, 4), (4, 5), (5, 8), (9, 10)]
W = 20
print knapsack(W, Elements)