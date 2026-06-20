class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lpv, rpv = 0, len(numbers)-1
        for i in range(len(numbers)):
            left_pointer, right_pointer = numbers[lpv], numbers[rpv]
            if left_pointer + right_pointer < target:
                lpv += 1
            elif left_pointer + right_pointer > target:
                rpv -= 1
            else:
                return [lpv+1, rpv+1]

        