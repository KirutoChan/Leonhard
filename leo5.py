# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_multiple(n):
	current = None
	last = 1
	bd = 1
	for i in range(2, n + 1):
		current = i
		if current % last == 0:
			bd = current
			last = i
			print ('bd = ', bd)
		else:
			j = 2
			while (current * j) % bd != 0:
				j = j + 1
			bd = current * j
			#current = bd
			last = i	
			print ('BD = ', bd, current)
	return bd

		
print (smallest_multiple(20))



# toliau bandyta surasti visus prime factor, nors to uzduociai nereikia

def prime_numbers(n):
	list = []					 	
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
	return prime_factors

def all_factors(n):		
# Suraso visus pirminius skaicius, kuriuos sudauginus gaunam norima skaiciu, 
# pvz.: 8 = 2 x 2 x 2, t.y. [2, 2, 2]							
	all_factors = {}
	for i in range (1, n + 1):							
		#jei skaicius pirminis arba jei factoriu ir yra tiek, kiek prime(i):
		p = 1
		for k in range(len(prime(i)) - 1, -1, -1):
			p = p * prime(i)[k]
		if p == i:
			all_factors[i] = prime(i)
		# jei faktoriu yra daugiau nei gauta is prime(i):
		else:
			all_factors[i] = [prime(i)[-1]]
			next = int(i / prime(i)[-1])
			if next == prime(i)[0]:
				all_factors[i].append(prime(i)[0])
			else:
				while next != 1:
					for k in range(len(prime(i)) - 1, -1, -1):
						if next % prime(i)[k] == 0:
							all_factors[i].append(prime(i)[k])
							next = int(next / prime(i)[k])	
	for i in all_factors:
		print (i, ':', all_factors[i])			
	return all_factors









