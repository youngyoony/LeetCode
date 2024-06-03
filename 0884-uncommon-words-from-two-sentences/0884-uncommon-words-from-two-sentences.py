class Solution:
    def uncommonFromSentences(self, s1, s2):
        word_count = {}
        
        def add_words(sentence):
            for word in sentence.split():
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        
        add_words(s1)
        add_words(s2)
        
        return [word for word in word_count if word_count[word] == 1]