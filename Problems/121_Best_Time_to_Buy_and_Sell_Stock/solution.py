class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        min_price = float('inf')     #a large enough number to exceed the data limits of the task
        max_profit = 0
        for price in prices:    #sliding window algorithm
            if price < min_price:
                min_price = price
            else:
                if price - min_price > max_profit:
                    max_profit = price - min_price
        return max_profit