# Given a 2D grid of size m x n and an integer k. You need to shift the grid k 
# times. 
# 
#  In one shift operation: 
# 
#  
#  Element at grid[i][j] moves to grid[i][j + 1]. 
#  Element at grid[i][n - 1] moves to grid[i + 1][0]. 
#  Element at grid[m - 1][n - 1] moves to grid[0][0]. 
#  
# 
#  Return the 2D grid after applying shift operation k times. 
# 
#  
#  Example 1: 
#  
#  
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[9,1,2],[3,4,5],[6,7,8]]
#  
# 
#  Example 2: 
#  
#  
# Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
# Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
#  
# 
#  Example 3: 
# 
#  
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
# Output: [[1,2,3],[4,5,6],[7,8,9]]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m <= 50 
#  1 <= n <= 50 
#  -1000 <= grid[i][j] <= 1000 
#  0 <= k <= 100 
#  
# 
#  Related Topics Array Matrix Simulation 👍 1512 👎 314

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        self.row = len(grid)
        self.col = len(grid[0])
        grid_size = self.row * self.col
        move_times = k % (grid_size)
        end = grid_size - move_times
        swap_space = []

        for i in range(end, grid_size):
            m, n = self.get_position_by_step(i)
            swap_space.append(grid[m][n])

        for i in range(end - 1, -1, -1):
            m, n = self.get_position_by_step(i)
            m1, n1 = self.get_position_by_step(i + move_times)
            grid[m1][n1] = grid[m][n]

        for i in range(move_times):
            m, n = self.get_position_by_step(i)
            grid[m][n] = swap_space[i]

        return grid

    def get_position_by_step(self, k):
        return k // self.col, k % self.col

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    param1 = [[1],[2],[3],[4],[7],[6],[5]]
    param2 = 23

    sol = Solution()
    result = sol.shiftGrid(param1, param2)
    assert result == [[6],[5],[1],[2],[3],[4],[7]]