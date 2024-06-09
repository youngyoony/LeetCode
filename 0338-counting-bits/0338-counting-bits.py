class Solution:
    def countBits(self, n):
        bitCount = [0] * (n + 1)
        
        for i in range(1, n + 1):
            bitCount[i] = bitCount[i & (i - 1)] + 1

        return bitCount