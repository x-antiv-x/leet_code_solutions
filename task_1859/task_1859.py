# LeetCode #1859 | Sorting the Sentence | [EASY]

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        words = s.split(" ")
        order = [""] * len(words)

        for w in words:
            o = int(w[-1])
            order[o-1] = w[:len(w)-1]

        return " ".join(order)