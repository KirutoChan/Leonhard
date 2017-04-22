import math
# def prime_numbers(n):
# 	good_list = [1, 2, 3]					
# 	for i in range(4, n + 1): 
# 		check_list = []
# 		k = int(math.sqrt(i))	
# 		for j in range(2, k + 1):        
# 			if i % j == 0:
# 				check_list.append(1)
# 			else:
# 				check_list.append(0)	
# 		check = 1
# 		if check not in check_list:
# 			good_list.append(i)	
# 	return good_list

def prime_numbers(n):
	prime_list = [2, 3]	
	i = 4				
	while len(prime_list) < n: 	    # n = n-th element in list of prime numbers
		check_list = []				# cheking if a number of interest (i) divides by any of number from 2 to sqrt(i)
		k = int(math.sqrt(i))	
		for j in range(2, k + 1):        
			if i % j == 0:
				check_list.append(1)
			else:
				check_list.append(0)	
		check = 1
		if check not in check_list:
			prime_list.append(i)	
		i = i + 1
	return prime_list[-1]


print (prime_numbers(101))