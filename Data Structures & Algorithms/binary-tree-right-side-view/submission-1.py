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

            right_most = 0 
            cnt = len(dq)

            for _ in range(cnt): 
                right_most = dq.popleft()

                if right_most.left: 
                    dq.append(right_most.left)
                if right_most.right: 
                    dq.append(right_most.right)
                    
            res.append(right_most.val)
        return res