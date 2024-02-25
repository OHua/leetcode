# Given an array of intervals where intervals[i] = [starti, endi], merge all 
# overlapping intervals, and return an array of the non-overlapping intervals that 
# cover all the intervals in the input. 
# 
#  
#  Example 1: 
# 
#  
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#  
# 
#  Example 2: 
# 
#  
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= intervals.length <= 10⁴ 
#  intervals[i].length == 2 
#  0 <= starti <= endi <= 10⁴ 
#  
# 
#  Related Topics Array Sorting 👍 16383 👎 585

from typing import List
import timeit
import random


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        atime = timeit.default_timer()
        # intervals = self.sortIntervals(intervals)
        intervals = self.quickSort(intervals)
        btime = timeit.default_timer()
        print(btime - atime)

        intervals = self._merge(intervals)
        intervals = self._merge2(intervals)
        ctime = timeit.default_timer()
        print(ctime - btime)
        return intervals

    def _merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for interval in intervals:
            overlaped = False
            for key in range(len(result)):
                if self.isOverlap(interval, result[key]):
                    newItem = self.mergeTwo(interval, result[key])
                    result[key] = newItem
                    overlaped = True
                    break
            if not overlaped:
                result.append(interval)
        return result


    [1, 3] , [1, 4]
    def _merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        current_left = intervals[0][0] #1
        current_right = intervals[0][1] #3
        for i in range(len(intervals)):
            if intervals[i][0] == current_left:
                current_right = intervals[i][1] if intervals[i][1] > current_right else current_right
            elif self.isOverlap([current_left, current_right], intervals[i]):
                current_left, current_right = self.mergeTwo([current_left, current_right], intervals[i])
            else:
                result.append([current_left, current_right])
                current_left = intervals[i][0]
                current_right = intervals[i][1]

        result.append([current_left, current_right])
        return result

    def isOverlap(self, item1: List[int], item2: List[int]) -> bool:


        if item1[1] < item2[0]:
            return False
        elif item1[0] > item2[1]:
            return False
        else:
            return True

    def mergeTwo(self, item1, item2):
        return [
            item1[0] if item1[0] < item2[0] else item2[0],
            item1[1] if item1[1] > item2[1] else item2[1],
        ]

    def sortIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        def compareTwoInterval(interval1, interval2):
            return interval1[0] > interval2[0]

        for i in range(len(intervals)):
            temp_key = i
            for j in range(i + 1, len(intervals)):
                if compareTwoInterval(intervals[temp_key], intervals[j]):
                    temp_key = j
            temp = intervals[i]
            intervals[i] = intervals[temp_key]
            intervals[temp_key] = temp

        return intervals

    def quickSort(self, intervals):
        if len(intervals) <= 1:
            return intervals

        pivot = intervals[-1]
        left_intervals = []
        right_intervals = []
        for i in intervals[:-1]:
            if i <= pivot:
                left_intervals.append(i)
            else:
                right_intervals.append(i)
        left_intervals = self.quickSort(left_intervals)
        right_intervals = self.quickSort(right_intervals)
        return left_intervals + [pivot] + right_intervals

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    sol = Solution()

    result = sol.quickSort([9,5,7,8,4,1,3,6,2])
    # print(result)
    assert result == [i for i in range(1,10)]


    param1 = [[1,3],[2,6],[8,10],[15,18]]
    result = sol.merge(param1)
    assert result == [[1,6],[8,10],[15,18]]

    param2 = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    result = sol.merge(param2)
    assert result == [[1,10]]

    param3 = [
        [i, i]
        for i in range(9999, 0, -1)
    ]
    random.shuffle(param3)

    result = sol.merge(param3)
    assert result == sorted(param3)
