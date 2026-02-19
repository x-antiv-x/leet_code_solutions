# LeetCode #3120 | Count the Number of Special Characters I | [EASY]

class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """

        chars = [ [False, False] for _ in range(26)]
        
        for char in word:
            x = ord(char)
            if x > 96:
                chars[x-97][1] = True
            else:
                chars[x-65][0] = True

        count = 0

        for char in chars:
            if ((char[0] == True) and (char[1] == True)):
                count += 1

        return count