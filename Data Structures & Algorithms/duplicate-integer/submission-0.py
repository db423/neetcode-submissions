class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_of_nums = []
        for item in nums:
            if item in list_of_nums:
                return True
            else:
                list_of_nums.append(item)
        return False