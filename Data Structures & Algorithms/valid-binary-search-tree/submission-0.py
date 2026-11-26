# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def _dfs(node,low, high):

            if not node: 
                return True
            
            if not (low < node.val < high):
                return False
            
            return _dfs(node.left,low,node.val) and _dfs(node.right,node.val,high)
        
        return _dfs(root, -float("inf"), float("inf"))
                