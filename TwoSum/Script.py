# This is my code for the "Two Sum" problem in LeetCode:
# Author: Shayan (Sean) Taheri

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

ex_nums = [2, 15, 11, 7]
ex_target = 9

myClass = Solution()

print(myClass.twoSum(ex_nums, ex_target))