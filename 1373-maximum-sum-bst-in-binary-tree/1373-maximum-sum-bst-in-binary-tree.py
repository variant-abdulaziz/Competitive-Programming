# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        book = {}
        ans = -float('inf')
        def populate(root):
            nonlocal ans
            if not root:
                return
            if not root.left and not root.right:
                ans = max(ans, root.val)
                book[root] = (root.val, True, root.val, root.val)
                return
            
            populate(root.left)
            populate(root.right)
            curr_sum, curr_is_bst, curr_min, curr_max = root.val, True, root.val, root.val
            if root.left:
                left_sum, left_is_bst, left_min, left_max = book[root.left]
                curr_sum += left_sum
                curr_is_bst = curr_is_bst and left_is_bst and left_max < root.val 
                curr_min = min(curr_min, left_min)
                curr_max = max(curr_max, left_max)
            
            if root.right:
                right_sum, right_is_bst, right_min, right_max = book[root.right]
                curr_sum += right_sum
                curr_is_bst = curr_is_bst and right_is_bst and right_min > root.val
                curr_min = min(curr_min, right_min)
                curr_max = max(curr_max, right_max)
            
            if curr_is_bst:
                ans = max(ans, curr_sum)
            book[root] = curr_sum, curr_is_bst, curr_min, curr_max
            
        populate(root)
        return max(ans, 0)
                