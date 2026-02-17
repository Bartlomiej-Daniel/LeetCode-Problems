# Remove Duplicates from Sorted Array

Category: Array / Two Pointers  
Difficulty: Easy

## Problem 
Given a sorted integer array `nums` (sorted in non-decreasing order), remove the duplicates **in-place** such that each unique element appears only once.  
The relative order of the elements should be kept the same.

Return the number of unique elements `k`.  
After calling the function, the first `k` elements of `nums` should contain the unique elements.  
The remaining elements of `nums` are not important.

## Constraints
- `0 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order

## Idea
Because the array is sorted, duplicate values are always placed next to each other.  
We can solve the problem using the **two pointers** technique:

- One pointer (`i`) iterates through the array.
- The second pointer (`k`) tracks the position where the next unique element should be placed.

Whenever we find a value different from the previous one, we overwrite the element at index `k` and move `k` forward.

## Algorithm
1. If the array is empty, return `0`.
2. Initialize `k = 1` (the first element is always unique).
3. Iterate from index `1` to the end of the array:
   - If `nums[i] != nums[i - 1]`, copy `nums[i]` to `nums[k]` and increment `k`.
4. Return `k`.

## Complexity
- Time complexity: O(n)
- Space complexity: O(1)
