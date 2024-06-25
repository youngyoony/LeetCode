class Solution:
    def sortSentence(self, s):

        words = s.split()
        
        sorted_words = [None] * len(words)
        
        for word in words:
            position = int(word[-1])
            sorted_words[position - 1] = word[:-1]
        
        return " ".join(sorted_words)