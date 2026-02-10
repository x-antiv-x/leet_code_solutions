# LeetCode #1897 | Redistribute Characters to Make All Strings Equal | [EASY]

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        
        req_freq = len(words)
        chars = [0]*26

        for word in words:
            for char in word:
                chars[ord(char)-97] += 1
            
        for char in chars:
            if (char % req_freq != 0):
                return False

        return True