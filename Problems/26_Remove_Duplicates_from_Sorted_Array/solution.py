class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0        #if nums has no elements, then it has no unique elements
        k = 1
        for i in range (1, len(nums)):
            if nums[i] != nums[i - 1]:      #checking if the current element has been repeated
                nums[k] = nums[i]
                k += 1
                
        return k
