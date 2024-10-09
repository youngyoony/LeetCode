class Solution:
     def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        S = str(x)
        i = 0
        j = len(S) - 1

        while i < j:
            if S[i] != S[j]:
                return False
            i += 1
            j -= 1

        return True