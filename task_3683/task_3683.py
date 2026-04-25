# LeetCode #3683 | Earliest Time to Finish One Task | [EASY]

class Solution(object):
    def earliestTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        
        earliest_ttf = tasks[0][0] + tasks[0][1]

        for t in tasks:
            ttf = t[0] + t[1]
            earliest_ttf = min(earliest_ttf, ttf)
        
        return earliest_ttf