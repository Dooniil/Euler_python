def search_sum():
	'''This program gives result like sum of numbers 
less 1000 and divisible by 3 and 5'''
	
	sum = 0
	for i in range (1, 1000):
		if i % 3 == 0 or i % 5 == 0:
			sum += i
	return sum
print(search_sum.__doc__)
print(search_sum());