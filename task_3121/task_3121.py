# LeetCode #3121 | Count the Number of Special Characters II | [MEDIUM]

class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        chars = [ [-1,-1] for _ in range(26) ]

        for i in range(len(word)):
            x = ord(word[i])

            if (x>96):
                chars[x-97][1] = i
            else:
                if (chars[x-65][0] == -1):
                    chars[x-65][0] = i
        
        count = 0
        
        for char in chars:
            if ((char[0] != -1) and (char[1] != -1) and (char[0] > char[1])):
                count += 1

        return count