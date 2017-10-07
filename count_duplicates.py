def count_duplicates(root):
    queue = [root]
    seen = {}
    duplicates = 0
    
    if root == None:
        return 0
    
    while len(queue) != 0:
        parent = queue.pop(0)
        if parent.val in seen:
            if seen[parent.val] == 1:
                duplicates += 1
            seen[parent.val] += 1
        else:
            seen[parent.val] = 1
        if parent.left != None:
            queue.append(parent.left)
        if parent.right != None:
            queue.append(parent.right)
    #print seen
    return duplicates

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(2)
D = TreeNode(4)

A.right = B
A.left = C
C.left = D
assert count_duplicates(A) == 1
assert count_duplicates(None) == 0

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
A.right = B
A.left = C
C.left = D
assert count_duplicates(A) == 0

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(2)
D = TreeNode(2)
A.right = B
A.left = C
C.left = D
assert count_duplicates(A) == 1
A = TreeNode(1)
B = TreeNode(1)
C = TreeNode(2)
D = TreeNode(2)
A.right = B
A.left = C
C.left = D
assert count_duplicates(A) == 2