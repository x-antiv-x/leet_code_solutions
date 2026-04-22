# LeetCode #1816 | Truncate Sentence | [EASY]

class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        w = s.split(" ")
        return " ".join(w[:min(len(w), k)])