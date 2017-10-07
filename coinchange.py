def coinChange(coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #key = amount left, value = minimum coins to get to that value 
        #base case
        #edge cases:
        possible = float("INF")
        if len(coins) == 0:
        	return 0
        #start from 0 and continue until we get to amount
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in answer:
            return answer[amount]

        for coin in coins:
        	amount_left = amount - coin
        	possible_answer = coinChange(coins, amount_left)
        	if possible_answer >= 0:
                possible = min(possible, 1 + possible_answer)
        return possible
print coinChange([1, 3, 2, 4], 11)

# def coinChange_helper(coins, total):
#     #start from 0 and go up until total
#     answer = {} #key = amount of money so far, value = min num of coins to get there
#     answer[0] = 0
#     amount = 0
#     possible = 0
#     count = 0
#     while amount != total:
#         if count == 2**(len(total))*total:
#             return -1
#         for coin in coins:
#             if amount > total: #case 1: amount > total, start again
#             #start again
#                 amount = 0
#                 possible = 0
#             #build up dictionary total
#             print amount
#             possible = answer[amount] + 1
#             amount += coin
#             if amount < total: #case 2: amount < total, continue
#             #keep building up
#                 if amount in answer:
#                     answer[amount] = min(answer[amount], possible)
#                 else:
#                     answer[amount] = possible
#         count += 1

#     if amount == total:
#         return answer[amount]

#     #edge case
#     #every coin combo is negative 

# def coinChange(coins, total):
# for coin in coins:    
#     if amount == total:
#         return answer[total]
#     print answer
#     return answer[total]

print coinChange([1, 3, 2, 4], 11)


