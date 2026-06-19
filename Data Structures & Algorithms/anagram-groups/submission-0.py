class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_counts = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            letter_counts[tuple(count)].append(word)
        return list(letter_counts.values())