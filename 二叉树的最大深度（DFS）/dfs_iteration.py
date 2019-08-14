# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:      
        #迭代版本：时间复杂度和空间复杂度都为O(N)
        #利用栈的数据结构
        stack = []
        #如果给的树不是空的，就给栈里传入深度1，以及树，即（1，root）
        if root is not None:
            stack.append((1, root))
        
        #初始一个深度为0，迭代到栈为空
        depth = 0
        while stack != []:
            #每次弹出最后一个元素，比如第一次弹出（1，root）
            current_depth, root = stack.pop()
            #如果root不是空，则继续
            if root is not None:
                #挑选出弹出的深度和目前的深度哪个值大，这就保证了如果某个子树的深度没有已知深度深，就不会保存
                depth = max(depth, current_depth)
                #因为root不是空，所以把root的左右节点都传入栈中，左右节点中有空也无所谓，是空的话不会进到这个判断里。
                #但会改变current depth的值
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        
        return depth