class Solution:
    def distributeCandies(self, candyType):
        total_candies = len(candyType)
        
        allowed_count = total_candies // 2
        
        unique_candies = set(candyType)
        
        max_types = len(unique_candies)
        
        return min(allowed_count, max_types)