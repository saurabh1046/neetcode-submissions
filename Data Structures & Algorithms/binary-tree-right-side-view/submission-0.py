# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root : 
            return []
        dq = deque([root])

        res = []

        while dq: 

            level_nodes = []
            cnt = len(dq)

            for _ in range(cnt): 
                node = dq.popleft()

                if node.left: 
                    dq.append(node.left)
                if node.right: 
                    dq.append(node.right)
                
                level_nodes.append(node.val)
            
            res.append(level_nodes[-1])
        return res