class Solution:
    def subsetXORSum(self, nums):
        def xorOfSubset(start, currentXOR):
            totalXOR = currentXOR
            for i in range(start, len(nums)):
                totalXOR += xorOfSubset(i + 1, currentXOR ^ nums[i])
            return totalXOR
        
        return xorOfSubset(0, 0)