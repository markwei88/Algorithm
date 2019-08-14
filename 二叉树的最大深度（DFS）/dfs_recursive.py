# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #递归版本：深度优先遍历，时间复杂度为O(N)，空间复杂度最坏是O(N)，最优是log(N)
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 