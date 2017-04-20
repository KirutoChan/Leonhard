# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

	
def is_polindrome(n):
	n_list = []
	p_list = []
	for i in str(n):
		n_list.append(i)

	for i in range(len(n_list) - 1, -1, -1):
		p_list.append(n_list[i])

	if n_list == p_list:
		return True
	return False
		
def polindrome_numbers(n):
	polindromes = []
	for i in range(999, 99, -1):
		for j in range(999, 99, -1):
			s = i * j
			if is_polindrome(i * j):
				polindromes.append(s)
	return max(polindromes)



print (is_polindrome(33))
print (polindrome_numbers(1))
