class Solution:
    def mergeAlternately(self, word1, word2):
        merged_string = []
        
        max_length = max(len(word1), len(word2))
        
        for i in range(max_length):
            if i < len(word1):
                merged_string.append(word1[i])
            if i < len(word2):
                merged_string.append(word2[i])
        
        return ''.join(merged_string)