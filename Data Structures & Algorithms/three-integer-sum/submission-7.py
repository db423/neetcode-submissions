class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = []
        nums = sorted(nums)
        for i in range(len(nums)):
            lpv, rpv = 0, len(nums) - 1
            while lpv < rpv:
                if lpv == i:
                    lpv += 1
                elif rpv == i:
                    rpv -= 1
                elif nums[lpv] + nums[rpv] < -nums[i]:
                    lpv += 1
                elif nums[lpv] + nums[rpv] > -nums[i] :
                    rpv -= 1
                else:
                    app = sorted([nums[lpv],nums[i],nums[rpv]])
                    if app not in lst:
                        lst.append(app)
                    lpv += 1
                    rpv -= 1
        return lst
