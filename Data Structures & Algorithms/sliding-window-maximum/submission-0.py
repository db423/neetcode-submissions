class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lst_of_mx = []
        for i in range(len(nums) - k + 1):
            sb_lst = nums[i:i+k]
            lst_of_mx.append(max(sb_lst))
        return lst_of_mx
