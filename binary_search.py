def binary_search(array, elt):
	start = 0
	end = len(array)
	center = len(array)/2

	while start <= end:
		center = (end+start)/2
		if array[center] < elt:
			start = center + 1

		elif array[center] > elt:
			end = center - 1
		else:
			return center

	return None

#test cases

print binary_search([1, 2, 3, 4, 5, 6], 3) 

