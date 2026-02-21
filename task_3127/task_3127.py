# LeetCode #3127 | Make a Square with the Same Color | [EASY]

class Solution(object):
    def canMakeSquare(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        
        box = [0,0,0,0]

        box[0] = sum(map(lambda char: 1 if (char == "W") else 0, [grid[0][0], grid[0][1], grid[1][0], grid[1][1]]))
        box[1] = sum(map(lambda char: 1 if (char == "W") else 0, [grid[1][0], grid[1][1], grid[2][0], grid[2][1]]))
        box[2] = sum(map(lambda char: 1 if (char == "W") else 0, [grid[0][1], grid[1][1], grid[0][2], grid[1][2]]))
        box[3] = sum(map(lambda char: 1 if (char == "W") else 0, [grid[1][1], grid[2][1], grid[1][2], grid[2][2]]))

        for b in box:
            if (b!=2):
                return True
                
        return False