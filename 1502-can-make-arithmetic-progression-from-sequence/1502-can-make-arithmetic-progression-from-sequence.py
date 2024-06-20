class Solution:
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        
        common_difference = arr[1] - arr[0]
        
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != common_difference:
                return False
        
        return True