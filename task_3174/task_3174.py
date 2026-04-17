# LeetCode #3174 | Clear Digits | [EASY]

class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        alpha = []

        for char in s:
            if (not char.isnumeric()):
                alpha.append(char)
            elif (alpha):
                alpha.pop()
        
        return "".join(alpha)
        