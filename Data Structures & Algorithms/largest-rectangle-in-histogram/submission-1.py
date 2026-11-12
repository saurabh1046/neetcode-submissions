class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] # index, height
        max_area = 0 

        for i, h in enumerate(heights): 

            start_index  = i
            while stack and stack[-1][1] > h : 
                # pop and caluculate 
                prev_index , prev_height = stack.pop()

                area = (i - prev_index) * prev_height
                max_area = max(area, max_area)

                start_index = prev_index


            stack.append([start_index,h])
        
        while stack : 
            prev_index , prev_height = stack.pop()
            area = (len(heights) - prev_index) * prev_height
            max_area = max(area, max_area)

        return max_area