# LeetCode #1572 | Matrix Diagonal Sum | [EASY]

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
        n = len(mat)
        s = 0

        for i in range(n):
            s += mat[i][i] + mat[i][n-i-1]

        if (n % 2 == 1):
            s -= mat[n // 2][n // 2]

        return s
 