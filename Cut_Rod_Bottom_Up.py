def Cut_Rod_Bottom_up(p, n):
	r = [0 for i in range(n + 1)]
	seg = [[] for i in range(n + 1)]
	for i in range(1, n + 1):
		q = max((p[j - 1] + r[i - j], seg[i - j], j) for j in range(1, i + 1))
		r[i] = q[0]
		seg[i] = q[1][:]
		seg[i].append(q[2])
	return r[n], seg[n]

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print Cut_Rod_Bottom_up(p, 9)