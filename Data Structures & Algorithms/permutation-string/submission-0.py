class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sub string in s2 should be equal to len of s1 
        # exact char should match (HashMap)

        if len(s1) > len(s2): 
            return False
        count_s1 = dict(Counter(s1))
        count_s2 = {}

        left = 0 
        for right in range (len(s2)): 
            char = s2[right]
            count_s2[char] = count_s2.get(char,0) + 1

            while right - left + 1 > len(s1): 
                count_s2[s2[left]] -= 1
                if count_s2[s2[left]] == 0 : 
                    del count_s2[s2[left]]
                left += 1 

            if count_s1 == count_s2 : 
                return True
        return False 