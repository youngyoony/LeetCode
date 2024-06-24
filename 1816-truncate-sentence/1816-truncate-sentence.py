class Solution:
    def truncateSentence(self, s, k):
        words = s.split()
        
        truncated_words = words[:k]
        
        truncated_sentence = ' '.join(truncated_words)
        
        return truncated_sentence