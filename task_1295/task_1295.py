# LeetCode #1295 | Find Numbers with Even Number of Digits | [EASY]

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0

        for n in nums:
            digits = 0
            
            while(n != 0):
                n = n // 10
                digits += 1

            if (digits % 2 == 0):
                count += 1
        
        return count