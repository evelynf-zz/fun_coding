
def phone_helper(numbers):
	alpha = {2:["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"]} #dictionary mapping num to letters
	#base case
	total_comb = []
	#base case
	if len(numbers) == 0:
		return [""]

	for digit in numbers:
		for letter in alpha[int(digit)]:
			word = phone_helper(numbers[1:])
			for i in range(len(word)):
				word[i] = letter + word[i]
			total_comb = total_comb + word
		return total_comb
	return total_comb

print phone_helper("234")

def phone_helper(numbers):
	alpha = {2:["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"]} #dictionary mapping num to letters
	#base case
	total_comb = []
	#base case
	if len(numbers) == 0:
		return [""]

	for digit in numbers:
		for letter in alpha[int(digit)]:
			words = phone_helper(numbers[1:])
			for word in words:
				word = letter + word
				total_comb.append(word)
		return total_comb
	return total_comb

print phone_helper("234")