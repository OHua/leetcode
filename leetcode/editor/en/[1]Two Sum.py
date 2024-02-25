# Given an array of integers nums and an integer target, return indices of the 
# two numbers such that they add up to target. 
# 
#  You may assume that each input would have exactly one solution, and you may 
# not use the same element twice. 
# 
#  You can return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [3,3], target = 6
# Output: [0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 10⁴ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  Only one valid answer exists. 
#  
# 
#  
# Follow-up: Can you come up with an algorithm that is less than 
# O(n²) time complexity?
# 
#  Related Topics Array Hash Table 👍 37795 👎 1205


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_map = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need not in my_map.keys():
                my_map[nums[i]] = i
            else:
                return my_map[need], i

        
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    param1 = [2,7,11,15]
    parma2 = 9

    sol = Solution()
    ret = sol.twoSum(param1, parma2)

    assert ret == (0,1)