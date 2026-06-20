class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)# the index of latest instance of letter + 1
            mp[s[r]] = r # update the index of latest instance of letter
            res = max(res, r - l + 1)
        return res