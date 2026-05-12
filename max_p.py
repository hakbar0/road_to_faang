class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, max_p = 0, 1, 0

        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff > 0:
                max_p = max(max_p, diff)
            else:
                l = r
            
            r += 1
        
        return max_p
    