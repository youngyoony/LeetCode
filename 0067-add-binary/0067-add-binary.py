class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        
        max_length = max(len(a), len(b))
        a = a.zfill(max_length)
        b = b.zfill(max_length)
        
        for i in range(max_length - 1, -1, -1):
            total_sum = int(a[i]) + int(b[i]) + carry
            carry = total_sum // 2
            result.append(str(total_sum % 2))
        
        if carry:
            result.append('1')
        
        return ''.join(result[::-1])
