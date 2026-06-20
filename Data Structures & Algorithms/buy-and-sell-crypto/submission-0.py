class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lpv, rpv = 0, len(prices) - 1
        highest_pft = 0
        for i in range(len(prices)):
            cur_price = prices[i]
            sell_vals = prices[i:]
            if sell_vals:
                max_prft = max(sell_vals) - cur_price
                highest_pft = max(max_prft, highest_pft)
            
        return highest_pft

