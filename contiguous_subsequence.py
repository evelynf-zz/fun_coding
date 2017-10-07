# Given a sequence of n real numbers A(1) ... A(n), determine a contiguous subsequence A(i) ... A(j) for which the sum of elements in the subsequence is maximized.

#A[i,j] = sum of the elements from A[i] to A[j]
#T[i, j] = max(T[i, j-1] + A[j], T[i+1, j] + A[i], T[i+1, j-1], ) 


# A: [a_1, a_2, a_3, a_4, ......a_n]

# T: [ a_1, max(a_2 + T[0], a_2), max(a_3 + T[1], a_3),   ,   ,  
    
# Looking at a_1
# T[0] = a_1

# Looking at a_2
# Allowed variables: i, a_2, T[0]
# T[1] = max(a_2 + T[0], a_2)

# Looking at a_3
# 

# Looking at a_n
# Allowed variables: n, a_n, T[n-1], 
# T[n] = max(a_n + T[n-1], a_n)


def contiguous_subseq(numbers):
    T = [None]*len(numbers)
    start = 0
    maximum = -float("inf")
    end = 0
    #base case
    if len(numbers) == 0:
        return None
    T[0] = (numbers[0], start)
    
    for i in range(1, len(numbers)):
        a_i = numbers[i]
        if a_i + T[i-1][0] > a_i:
            start = T[i-1][1]
        else:
            start = i
        T[i] = (max(a_i + T[i-1][0], a_i), start)

    for j in range(len(T)):
        if T[j][0] > maximum:
            (maximum, start) = T[j]
            end = j
            
    return (start, end)

#test cases
assert contiguous_subseq([1, 2, 3, 4, -10]) == (0, 3)
assert contiguous_subseq([1, -10, 3, 4, -10]) == (2, 3)
assert contiguous_subseq([]) == None
assert contiguous_subseq([-10, -10, -10, 1]) == (3, 3)
assert contiguous_subseq([-10, -10, -10]) == (0, 0)
assert contiguous_subseq([-10, 1, -10]) == (1, 1 )