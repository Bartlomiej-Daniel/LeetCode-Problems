from solution import Solution

def test_twoSum():
    solution = Solution() 
    #Test 1: the first one does not change 
    nums = [2,7,11,15] 
    target = 9 
    assert set(solution.twoSum(nums, target)) == {0,1} 

    #Test 2: the second one does not change 
    nums = [3,2,4] 
    target = 6 
    assert set(solution.twoSum(nums, target)) == {1,2} 
    
    #Test 3: only two element 
    nums = [3,3] 
    target = 6 
    assert set(solution.twoSum(nums, target)) == {0,1} 
    
    #Test 4: first and last 
    nums = [3,1,2,4,5,8] 
    target = 11 
    assert set(solution.twoSum(nums, target)) == {0,5}

    #Test 5: negatives
    nums = [-3, 4, 3, 90]
    target = 0
    assert set(solution.twoSum(nums, target)) == {0,2}

    #Test 6: complement equals same element value but there are duplicates
    nums = [1, 5, 1, 7]
    target = 2
    assert set(solution.twoSum(nums, target)) == {0,2}

    #Test 7: large values
    nums = [10**9, 1, 2, -10**9]
    target = 0
    assert set(solution.twoSum(nums, target)) == {0,3}