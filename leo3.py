import math
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def primenumbers(n):
	list = []
	for i in range(1, int(math.sqrt(n))):
		if i % 2 != 0 or i == 2:
			list.append(i)
	return list

def prime(n):
	used = []
	for i in primenumbers(n):
		new = n / i
		if n % i == 0 and i != 1:
			used.append(i)
			n = new
	print (used)
	return max(used)


print (prime(600851475143)) 



			


