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
        prevMap = {}  # val -> index ( this will store integers we seen within the array for the indices as values)

        for i, n in enumerate(nums): # This will iterate in a loop fashion with "enumerate" meaning it will list it one by one individually for (nums)
            diff = target - n # getting the difference between the target and the current number with "n"
            if diff in prevMap: # if "diff" is in the hashmap, it means we've found a pair that adds up to the target
                return [prevMap[diff], i] # returning the indices of the 2 numbers
            prevMap[n] = i # add the current number "n" and the index "i" to the hashmap for future reference

