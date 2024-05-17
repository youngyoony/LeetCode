class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x):

        def sum_of_digits(n):
            return sum(int(digit) for digit in str(n))
        
        digit_sum = sum_of_digits(x)
        
        if x % digit_sum == 0:
            return digit_sum
        else:
            return -1

# 예시 사용
sol = Solution()
print(sol.sumOfTheDigitsOfHarshadNumber(18))  # 출력: 9
print(sol.sumOfTheDigitsOfHarshadNumber(23))  # 출력: -1