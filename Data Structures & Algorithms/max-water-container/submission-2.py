class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lpv, rpv = 0, len(heights) - 1
        maxarea = 0
        if lpv <= rpv:
            for i, n in enumerate(heights):
                area = (rpv - lpv) * min(heights[lpv],heights[rpv])
                maxarea = max(area, maxarea)
                if heights[lpv] <= heights[rpv]:
                    lpv += 1
                elif heights[lpv] > heights[rpv]:
                    rpv -= 1
        return maxarea

