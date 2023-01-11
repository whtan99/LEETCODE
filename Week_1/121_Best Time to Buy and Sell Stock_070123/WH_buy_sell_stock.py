class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        high = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > low:
                profit = max(profit, prices[i] - low)
            else:
                low = prices[i]
        return profit
