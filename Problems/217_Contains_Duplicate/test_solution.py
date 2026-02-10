from solution import Solution

def test_containsDuplicate():
    solution = Solution()

    #Test 1: first and last, one duplicate
    nums = [1,2,3,1]
    assert solution.containsDuplicate(nums) == True

    #Test 2: no duplicates
    nums = [1,2,3,4]
    assert solution.containsDuplicate(nums) == False

    #Test 3: only one number
    nums = [1,1,1,1]
    assert solution.containsDuplicate(nums) == True

    #Test 4: size 2 list
    nums = [1,1]
    assert solution.containsDuplicate(nums) == True

    #Test 5: many duplicates
    nums = [1,1,1,3,3,4,3,2,4,2]
    assert solution.containsDuplicate(nums) == True

    #Test 6: empty list 
    nums = []
    assert solution.containsDuplicate(nums) == False

    #Test 7: negatives and zeros
    nums = [-1, 0, 1, -1]
    assert solution.containsDuplicate(nums) == True

