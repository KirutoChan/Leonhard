import math
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def prime_numbers(n):
	list = []					 
	n = int(math.sqrt(n))			# doesn't fit for ex. n = 1002 (should be 167 the largest, but it's three)
	
	for i in range(1, n + 1):           
		if i % 2 != 0 or i == 2:
			list.append(i)		
	return list

def prime(n):
	prime_factors = []
	for i in prime_numbers(n):
		new = n / i
		if n % i == 0 and i != 1:
			prime_factors.append(i)
			n = new
	if prime_factors == []:				# checks if the number is already prime itself
		return [n]
	if n % 2 != 0 and n != 1:			# because we check only that prime numbers which are under sqrt(n), the last n isn's compared to list_prime (it's larger), so we check if it is prime or not, and if yes, add to prime factors list
		prime_factors.append(int(n))
	print (prime_factors)
	
	return max(prime_factors)


print (prime(600851475143)) 
print (prime(100000000002)) 
print (prime(1002)) 
print (prime(15)) 








			


