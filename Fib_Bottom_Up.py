def fibonacci(n):
	memo = {}
	for i in range(1, n + 1):
		if i <= 2:
			memo[i] = 1
		else:
			memo[i] = memo[i - 1] + memo[i - 2]
	return memo[n]

print fibonacci(8)