class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list) -> str:
        normalized_plate = ''.join([char.lower() for char in licensePlate if char.isalpha()])
        
        def get_letter_count(s):
            letter_count = {}
            for letter in s:
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
            return letter_count
        
        plate_count = get_letter_count(normalized_plate)
        
        shortest_word = None
        
        for word in words:
            word_count = get_letter_count(word)
            
            matches = True
            for char in plate_count:
                if word_count.get(char, 0) < plate_count[char]:
                    matches = False
                    break
            
            if matches:
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word
        
        return shortest_word