# Given an integer array "nums", return "true" if any value appears more than once in the array, otherwise "return false"

nums = [1, 2, 3, 4,]

#Output: true

nums = [1, 2, 2, 3]

#Output: false


List = [1, 2, 3, 4]

class Solution:
    def hasDuplicate(self, nums: List[int]) bool:
        hashset = set() # This hashset is like a shoe box that orders all the shoes in a organized matter and it checks for duplicates

        for n in nums: # for all the n's in the integer array "nums"
            if n in hashset: # if n "integers" in the hashset is all ordered and no duplicates
                return True # Return the output to true for the boolean
            hashset.add(n) #  this is used to add the integer n to the hashset shoe box to find any extra integer duplicates
            return False # return false if there is a integer that repeats so the output would return false
