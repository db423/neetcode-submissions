class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        no_letters_map = defaultdict(int)
        for letter in s1:
            no_letters_map[letter] = 1 + no_letters_map.get(letter, 0)
        # We have a map depicting the letters and quantity. 
        l = 0
        substring_map = defaultdict(int)
        for r in range(1, len(s2)+1):
            substring = s2[l:r]
            if len(substring) > len(s1):
                l += 1
                substring_map[substring[0]] = substring_map.get(substring[0]) - 1
                if substring_map[substring[0]] == 0:
                    del substring_map[substring[0]]
            new_letter = substring[-1]
            substring_map[new_letter] = 1 + substring_map.get(new_letter, 0)
            if substring_map == no_letters_map:
                return True
        
        return False



