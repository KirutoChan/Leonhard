def sum_square(n):
	sum_square = 0
	s = 0
	for i in range(1, n + 1):
		sum_square = sum_square + i**2
		s = s + i
	result = s ** 2 - sum_square
	return result

print (sum_square(100))
