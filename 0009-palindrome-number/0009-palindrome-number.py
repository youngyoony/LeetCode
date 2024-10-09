class Solution:
     def isPalindrome(self, x: int) -> bool:
        # 음수는 회문이 될 수 없으므로 바로 False 반환
        if x < 0:
            return False
        
        # 숫자를 문자열로 변환
        S = str(x)
        i = 0
        j = len(S) - 1

        while i < j:
            if S[i] != S[j]:
                return False
            i += 1
            j -= 1

        return True