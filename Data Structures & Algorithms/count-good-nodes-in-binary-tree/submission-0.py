# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def _dfs(node, value): 
            if not node : 
                return 0 
            
            new_val = max(value, node.val)

            left_cnt = _dfs(node.left, new_val)
            right_cnt = _dfs(node.right, new_val)

            total_cnt = left_cnt + right_cnt + (1 if node.val >= value else 0)

            return total_cnt
        
        return _dfs(root,root.val)




        