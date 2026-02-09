# Length of Last Word

**Category:** String  
**Difficulty:** Easy

## Problem

Given a string consisting of words and spaces, return the length of the last word.
A word is defined as a sequence of non-space characters.

## Constraints:

* 1 <= s.length <= 104
* s consists of only English letters and spaces ' '.
* There will be at least one word in s.

## Idea

The last word may be followed by trailing spaces.  
We can iterate from the end of the string, skip spaces, and then count characters until we reach another space or the beginning of the string.

## Algorithm

1. Start from the last character of the string.
2. Skip all trailing spaces.
3. Count characters until a space or index -1 is reached.
4. Return the counter.

## Complexity

* Time complexity: O(n)
* Space complexity: O(1)
