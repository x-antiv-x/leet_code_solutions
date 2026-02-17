# LeetCode #1160 | Find Words That Can Be Formed by Characters | [EASY]

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        
        available_chars = {}
        total_length = 0 
        
        for char in chars:
            available_chars[char] = available_chars.get(char, 0) + 1

        for word in words:
            present_chars = {}
            for char in word:
                present_chars[char] = present_chars.get(char, 0) + 1
            
            all_is_good = True

            for char, freq in present_chars.items():
                max_freq = available_chars.get(char, 0)
                if (freq > max_freq):
                    all_is_good = False
                    break
            
            total_length += len(word) if all_is_good else 0
        
        return total_length