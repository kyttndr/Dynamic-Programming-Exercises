def CUT_ROD(p, n):
	r = [0 for i in range(n + 1)]
	for i in range(n + 1):
		r[i] = -float("inf")
	seg = [[] for i in range(n + 1)]
	return MEMOIZED_CUT_ROD_AUX(p, n, r, seg)

def MEMOIZED_CUT_ROD_AUX(p, n, r, seg):
	if r[n] >= 0:
		return r[n]
	if n == 0:
		q = (0, [])
	else:
		q = max((p[i - 1], i) + MEMOIZED_CUT_ROD_AUX(p, n - i, r, seg) for i in range(1, n + 1))
	r[n] = q[0]
	seg[n] = q[1]
	return (r[n], seg[n])

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print CUT_ROD(p, 10)