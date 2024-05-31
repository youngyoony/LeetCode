class Solution:
    def findErrorNums(self, nums):
        duplicate = -1
        missing = 1
        
        count = [0] * (len(nums) + 1)
        
        for num in nums:
            count[num] += 1
        
        for i in range(1, len(count)):
            if count[i] == 2:
                duplicate = i
            elif count[i] == 0:
                missing = i
        
        return [duplicate, missing]