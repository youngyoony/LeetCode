class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        def sum_of_digits(n):
            sumint = sum(int(digit) for digit in str(n))
            return sumint

        sumofdegits = sum_of_digits(x)

        if x % sumofdegits == 0:
            return sumofdegits   
        else:
            return -1   