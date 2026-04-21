# LeetCode #2651 | Calculate Delayed Arrival Time | [EASY]

class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """

        return (arrivalTime+delayedTime) % 24
        