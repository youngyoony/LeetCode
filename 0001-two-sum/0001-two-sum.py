class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = {}

        for i, num in enumerate(nums):
            num_minus = target - num

            if num_minus in num_list:
                return [num_list[num_minus], i]

            num_list[num] = i