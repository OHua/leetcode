# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[
# k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
# 
#  Notice that the solution set must not contain duplicate triplets. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not 
# matter.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
# 
#  Related Topics Array Two Pointers Sorting 👍 22533 👎 2057

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)):
            need = nums[i]*(-1)
            candidate_nums = nums[i+1:]
            result = self.twoSum(candidate_nums, need)
            for r in result:
                ans.append([nums[i], candidate_nums[r[0]], candidate_nums[r[1]]])
        return ans

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        nums_length = len(nums)
        for i in range(nums_length):
            x = target - nums[i]
            for j in range(i+1, nums_length):
                if nums[j] == x:
                    result.append([i,j])
        return result
        
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    sol = Solution()
    param1 = [-1,0,1,2,-1,-4]
    result = sol.threeSum(param1)
    assert result == [[-1,-1,2],[-1,0,1]]