# Two Sum

**Category:** Arrays / Hash Table  
**Difficulty:** Easy

## Problem
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Idea
Use a hash map to remember elements we've seen so far (value -> index).
For each number `x`, check if `target - x` is already in the map — if yes, we found the pair.

## Algorithm (single-pass)
1. Initialize an empty map `seen`.
2. Iterate over `nums` with index `i` and value `num`.
3. Compute `complement = target - num`.
4. If `complement` is in `seen`, return `[seen[complement], i]`.
5. Otherwise store `seen[num] = i`.

## Complexity
- Time: `O(n)`
- Space: `O(n)`

