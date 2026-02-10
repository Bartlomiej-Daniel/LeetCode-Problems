# Contains Duplicate

**Category:** Arrays / Hash Table  
**Difficulty:** Easy

## Problem
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Idea
Track elements that we've seen so far in a set. If we encounter an element that is already in the set, we have a duplicate and can return early.

## Algorithm
1. Initialize an empty set `seen`.
2. Iterate through `nums`.
3. If current number is in `seen`, return `true`.
4. Otherwise add the number to `seen`.
5. If the loop completes, return `false`.

## Complexity
- Time: `O(n)` on average
- Space: `O(n)`

## Notes
- My first approach included sorting (`O(n log n)`), but this new implementation does not modify the input list
- Another approach could be to use `len(set(nums)) != len(nums)`, but then it would create the full set upfront.

