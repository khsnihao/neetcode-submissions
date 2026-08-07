class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n)
        table = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            if s[r] in table and table[s[r]] >= l:
                # abba as example, l should be at index 4 not 0
                # l = max(table[s[r]], l)
                l = table[s[r]] + 1
            table[s[r]] = r
            res = max(res, r-l+1)
        return res



