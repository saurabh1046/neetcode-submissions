# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_idx = {val: i for i , val in enumerate(inorder)}
        self.pre_idx = 0 


        def _build(in_left, in_right): 

            if in_left > in_right:
                return None
            

            val = preorder[self.pre_idx]
            mid = inorder_idx[val]

            node = TreeNode(val)
            self.pre_idx += 1 

            node.left = _build(in_left, mid - 1)
            node.right = _build(mid + 1,in_right)

            return node
        
        return _build(0 , len(inorder) - 1)
        
            

