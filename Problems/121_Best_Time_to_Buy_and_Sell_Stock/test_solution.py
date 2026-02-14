from solution import Solution

def test_maxProfit():
    solution = Solution()
    
    #test 1: standard case
    prices = [7,1,5,3,6,4]
    assert solution.maxProfit(prices) == 5
    
    #test 2: no profit
    prices = [7,6,4,3,1]
    assert solution.maxProfit(prices) == 0
    
    #test 3: too few days to buy and sell
    prices = [1]
    assert solution.maxProfit(prices) == 0
    
    #test 4: no price changes
    prices = [0,0,0,0,0]
    assert solution.maxProfit(prices) == 0
    
    #test 5: only one price change
    prices = [0,0,1,0,0]
    assert solution.maxProfit(prices) == 1

    #test 6: empty list
    prices = []
    assert solution.maxProfit(prices) == 0

    #test 7: buy on day 0 sell on last day
    prices = [1, 2, 3, 4, 5]
    assert solution.maxProfit(prices) == 4

    #test 8: large numbers
    prices = [10**9, 1, 10**9]
    assert solution.maxProfit(prices) == 10**9 - 1