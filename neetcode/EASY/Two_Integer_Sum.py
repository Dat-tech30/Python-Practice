'''Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.'''

"""
nums=[3,4,5,6]
target=7


nums=[4,5,6]
target=10

- Example Inputs:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]

Input: nums = [5,5], target = 10

Output: [0,1]




"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
