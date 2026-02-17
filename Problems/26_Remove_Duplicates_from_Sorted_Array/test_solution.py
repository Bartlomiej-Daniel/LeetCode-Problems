from solution import Solution

def test_removeDuplicates():
    solution = Solution()

    # Test 1: only one duplicate
    nums = [1,1,2]
    expectedNums = [1, 2]
    k = solution.removeDuplicates(nums)
    assert k == len(expectedNums)
    for i in range (k): 
         assert nums[i] == expectedNums[i]


    # Test 2: a lot of duplicates
    nums = [0,0,1,1,1,2,2,3,3,4]
    expectedNums = [0, 1, 2, 3, 4]
    k = solution.removeDuplicates(nums)
    assert k ==  len(expectedNums)
    for i in range (k): 
         assert nums[i] == expectedNums[i]
         
    # Test 3: no nums elements
    nums = []
    expectedNums = []
    k = solution.removeDuplicates(nums)
    assert k ==  len(expectedNums)
    for i in range (k): 
         assert nums[i] == expectedNums[i]
         
    # Test 4: only one item with multiple duplicates
    nums = [1, 1, 1, 1, 1]
    expectedNums = [1]
    k = solution.removeDuplicates(nums)
    assert k ==  len(expectedNums)
    for i in range (k): 
         assert nums[i] == expectedNums[i]
         
    # Test 5: only one item with no duplicates
    nums = [1]
    expectedNums = [1]
    k = solution.removeDuplicates(nums)
    assert k ==  len(expectedNums)
    for i in range (k): 
         assert nums[i] == expectedNums[i]

    # Test 6: all unique
    nums = [0,1,2,3,4,5]
    expected = [0,1,2,3,4,5]
    k = solution.removeDuplicates(nums)
    assert k ==  len(expectedNums)
    for i in range (k): 
         assert nums[i] == expectedNums[i]

    # Test 7: all negatives
    nums = [-3,-3,-2,-1,-1,0,0,1]
    expected = [-3,-2,-1,0,1]
    k = solution.removeDuplicates(nums)
    assert k ==  len(expectedNums)
    for i in range (k): 
         assert nums[i] == expectedNums[i]