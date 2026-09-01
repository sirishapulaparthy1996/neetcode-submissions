class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        longest = 0
        while r < len(prices):
            profit = 0
            if prices[r]>prices[l]:
                profit = prices[r] - prices[l]
            else:
                l = r
            r += 1
            longest = max(longest, profit)
        return longest

            







            




        