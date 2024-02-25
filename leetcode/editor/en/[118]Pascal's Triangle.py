# Given an integer numRows, return the first numRows of Pascal's triangle. 
# 
#  In Pascal's triangle, each number is the sum of the two numbers directly 
# above it as shown: 
#  
#  
#  Example 1: 
#  Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#  
#  Example 2: 
#  Input: numRows = 1
# Output: [[1]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= numRows <= 30 
#  
# 
#  Related Topics Array Dynamic Programming 👍 7934 👎 266

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        self.pascal_row_map = [
            [1],
            [1, 1],
        ]
        if numRows <= 2:
            return self.pascal_row_map[:numRows]
        else:
            self.generateToRow(numRows)
            return self.pascal_row_map[:numRows]

    def generateToRow(self, targetRow: int) -> List[int]:
        if targetRow > len(self.pascal_row_map):
            self.generateToRow(targetRow - 1)

        self.pascal_row_map.append([1])
        for i in range(len(self.pascal_row_map[targetRow - 1]) - 1):
            self.pascal_row_map[targetRow].append(
                self.pascal_row_map[targetRow - 1][i] + self.pascal_row_map[targetRow - 1][i + 1]
            )
        self.pascal_row_map[targetRow].append(1)
        
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    param = 5
    sol = Solution()
    result = sol.generate(param)
    assert result ==[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]