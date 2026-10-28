class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # conditons 
        # - window should have all the things in t - (hashmap for both)
        # - contiditon satified remvoe the elements form left still condition fails 
        # - continue and keep the track of min len

        if len(t) > len(s): 
            return ""

        target_map = dict(Counter(t))
        window_map = {}
        have,need = 0,len(target_map)

        min_len =float('inf')
        left_index = 0
        left = 0

        for right in range(len(s)): 

            char = s[right]

            window_map[char] = window_map.get(char,0) + 1 
            if char in target_map and window_map[char] == target_map[char]: 
                have += 1
            
            while have >= need:
                window_length = right - left + 1
                if min_len > window_length :
                    min_len = window_length
                    left_index = left
                
                left_char = s[left]
                window_map[left_char] -= 1
                if window_map[left_char] < target_map.get(left_char,0): 
                    have -= 1
                left += 1 
        return "" if min_len == float('inf') else s[left_index : left_index + min_len]       