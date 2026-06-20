class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        maxf, max_length, lpv = 0, 1, 0
        for i in range(len(s)):
            mp[s[i]] = 1 + mp.get(s[i], 0)
            maxf = max(maxf, mp[s[i]])
            while i - lpv + 1 - maxf > k:
                mp[s[lpv]] -= 1
                lpv += 1
            max_length = max(max_length, i - lpv + 1)
        return max_length
        
