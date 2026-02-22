# LeetCode #3151 | Special Array I | [EASY]

class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        rule = -1

        for num in nums:
            if (rule == -1):
                rule = num % 2
            else:
                if (rule == num % 2):
                    return False
                rule = num % 2
        
        return True