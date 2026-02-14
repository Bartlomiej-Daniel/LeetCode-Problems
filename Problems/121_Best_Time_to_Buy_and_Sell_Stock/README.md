# Best Time to Buy and Sell Stock

**Category:** Arrays / Dynamic Programming (greedy)  
**Difficulty:** Easy

## Problem
Given an array `prices` where `prices[i]` is the price of a given stock on day `i`,
return the maximum profit you can achieve from one transaction (buy once and sell once).
If no profit is possible, return `0`.

## Idea
I chose the sliding window algorithm because it has time complexity O(n) and space complexity O(1)

## Algorithm
1. Initialize `min_price = +inf` and `max_profit = 0`.
2. Iterate through `prices`.
3. If current price < `min_price`, update `min_price`.
4. Otherwise compute `price - min_price` and update `max_profit` if it's larger.
5. Return `max_profit`.

## Complexity
- Time: `O(n)` 
- Space: `O(1)`

## Notes
- At first I used a constant I assigned myself, which met the conditions of the task, but for greater generality I changed it to float('inf') and added tests with large numbers
- This solution is optimal for a single transaction. For multiple transactions or with cooldown/fees variants, the approach differs.


    
