class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        ordered_count = []
        for i,n in enumerate(nums):
            nums_count[n] = 1 + nums_count.get(n, 0)
        nums_count = sorted(nums_count, key = nums_count.get, reverse = True)
        return nums_count[:k]
     

