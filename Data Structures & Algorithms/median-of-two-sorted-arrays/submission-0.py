class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # binaray serach on one array figure out how much numbers to take form that array 
        # check if the  nums 1 -> mid  and  len(nums2) - mid (other elements from num2 )
        # follow the division by  such that mid and len(nums2) - mid << than other elements 

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)

        half = (m + n) // 2

        low, high = 0, m -1

        while True: 

            cut1 = low + (high - low) // 2 
            cut2 = half - cut1 - 2
            
            Aleft = nums1[cut1] if cut1 >= 0 else float("-inf")
            Aright = nums1[cut1 + 1] if (cut1 + 1) < m else float("inf")

            Bleft = nums2[cut2] if cut2 >= 0 else float("-inf")
            Bright = nums2[cut2 + 1] if (cut2 + 1) < n else float("inf")

            if Aleft <= Bright and Bleft <= Aright: 

                if (m + n) % 2 == 0 : 
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                
                return min(Aright , Bright)
            elif Aleft > Bright : 
                high = cut1 - 1
            else: 
                low = cut1 + 1 