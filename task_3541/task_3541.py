# LeetCode #3541 |  Find Most Frequent Vowel and Consonant | [EASY]

class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        v_freq = {"a": 0}
        c_freq = {"z": 0}

        for char in s:
            if (char in ["a","e","i","o","u"]):
                v_freq[char] = v_freq.get(char, 0) + 1
            else:
                c_freq[char] = c_freq.get(char, 0) + 1
        
        return max(v_freq.values()) + max(c_freq.values())
