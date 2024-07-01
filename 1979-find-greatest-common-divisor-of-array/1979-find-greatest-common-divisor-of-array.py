class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            if a < b:
                smaller = a
            else:
                smaller = b
            
            for i in range(smaller, 0, -1):
                if a % i == 0 and b % i == 0:
                    return i
        
        min_num = min(nums)
        max_num = max(nums)
        return gcd(min_num, max_num)