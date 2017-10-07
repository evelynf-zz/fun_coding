#You have a menu with appetizers, and $x to spend. What are the possible combinations of appetizers
#that you can order 
#loop through the foods in menu, and then find all of the possible combinations with x-food
#return a list for the foods
#order(3, [(apple, 1), (banana, 2), (cheese, 3)]
#apple order(2) ---> overal_total_1 = [[apple, apple, apple], [apple, banana]]
#		apple order(1) ---> overall_total_2 = [[apple, apple]]
#			apple order(0) ---> overall_total_3 = [[apple]]
#						[[]]
#			banana order(-1)
#						None
#			cheese order(-2)
#						None
#		banana order(0) ---> overall_total_2 = [[apple, apple], [banana]]
#
#				[[]]



#base case:
total = []
def order(x, menu):
	overall_total = []
	if x == 0:
		return [[]]
	if x < 0:
		print "Hi"
		return None
	for food in menu:
		new_foods = order(x-food, menu)
		if new_foods != None:
			print new_foods
			for comb in new_foods:
				comb = [food] + comb
				overall_total.append(comb)
	return overall_total

def order_food(x, menu):
	for food in menu:
		overall_total.append(order(x, menu))
	return overall_total

print order(7, [1, 2, 3, 4])



