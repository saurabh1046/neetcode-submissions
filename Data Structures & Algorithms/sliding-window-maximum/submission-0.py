class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0 
        res = []
        dq = deque([])
        for right in range(len(nums)): 
            while dq and nums[dq[-1]] <= nums[right]: 
                dq.pop()
            dq.append(right)
            
            if right - left + 1  > k :       
                if dq[0] == left: 
                    dq.popleft() 
                left += 1 

            if right - left + 1  == k : 
                res.append(nums[dq[0]])

        return res