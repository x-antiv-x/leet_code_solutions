# LeetCode #3726 | Remove Zeros in Decimal Representation | [EASY]

class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        m = 1
        while(n != 0):
            v = n % 10
            if (v != 0):
                s += v*m
                m *= 10
            n = n // 10
        return s
