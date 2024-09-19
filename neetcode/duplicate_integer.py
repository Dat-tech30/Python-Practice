# Given an integer array "nums", return "true" if any value appears more than once in the array, otherwise "return false"

nums = [1, 2, 3, 4,]

#Output: true

nums = [1, 2, 2, 3]

#Output: false


List = [1, 2, 3, 4]

class Solution:
    def hasDuplicate(self, nums: List[int]) bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
            return False
