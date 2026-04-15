# LeetCode #2652 | Sum Multiples | [EASY]

class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        total = 0
        for i in range(1,n+1):
            total += i if ((i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0 )) else 0
        return total