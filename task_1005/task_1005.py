# LeetCode #1005 | Maximize Sum Of Array After K Negations | [EASY]

class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort()
        first_non_negative_i= -1
        
        for i in range(len(nums)):
            if (k == 0):
                break
            elif (nums[i] < 0):
                nums[i] = -nums[i]
                k -= 1
            else:
                first_non_negative_i = i
                break

        if (not(k == 0) and not(nums[first_non_negative_i] == 0) and not(k % 2 == 0)):
            if (first_non_negative_i == 0):
                nums[first_non_negative_i] = -nums[first_non_negative_i] 
            else:
                if (abs(nums[first_non_negative_i]) > abs(nums[first_non_negative_i-1])):
                    nums[first_non_negative_i-1] = -nums[first_non_negative_i-1]
                else:
                    nums[first_non_negative_i] = -nums[first_non_negative_i] 
                
        return sum(nums)

    