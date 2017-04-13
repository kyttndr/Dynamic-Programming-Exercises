def CUT_ROD(p, n):
	r = [0 for i in range(n + 1)]
	for i in range(n + 1):
		r[i] = -float("inf")
	return MEMOIZED_CUT_ROD_AUX(p, n, r)

def MEMOIZED_CUT_ROD_AUX(p, n, r):
	if r[n] >= 0:
		return r[n]
	if n == 0:
		q = 0
	else:
		q = max(p[i - 1] + MEMOIZED_CUT_ROD_AUX(p, n - i, r) for i in range(1, n + 1))
	r[n] = q
	return r[n]

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print CUT_ROD(p, 10)