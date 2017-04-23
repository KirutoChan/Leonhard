# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math

def pythagor(n):
	for a in range(200, 351):				#approximately range(200 - 500) is choosed, 
		for b in range(500, 0, -1):			# "a" only till 351 which is (500-200)/2, to avoid repetitions
			c = math.sqrt(a**2 + b**2)
			if a + b + c == n:
				return int(a * b * c)
	return None

print (pythagor(1000))