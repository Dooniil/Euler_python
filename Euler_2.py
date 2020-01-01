def search_sum():
	'''This program counts sum of even 
elements of range or Fibbonachi until 4 mln'''

	element = 0
	f_element = 0
	s_element = 1
	summary = 0

	while element < 4000000:
		element = f_element + s_element
		f_element = s_element
		s_element = element
		if element % 2 == 0:
			summary += element

	return summary

print(search_sum.__doc__)
print("The summary = ", search_sum())