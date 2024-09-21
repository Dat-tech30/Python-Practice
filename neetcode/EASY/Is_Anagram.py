# Given two strings s and t, return "true" if the two strings are anagrams of each other, otherwise return "false".

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool
        if len(s) != len(t): # if len of "s" and len of t does not equal to each other return to False
            return False # Returning false in this case
        countS, countT = {}, {} # creates two empty dictionaries

        for i in range(len(s)): # for i in the range of the length of the s string it iterates throughout all the characters in the s string
            countS[s[i]] = 1 + countS.get(s[i], 0) # it increments it (increases) the count of the current characters using "s[i]" in the countS dictionary, if it does not exist in the dictionary add 1 to the count
            countT[t[i]] = 1 + countT.get(t[i], 0) # same thing but with t
        return countS == countT #compares the dictionaries if it's the same return true and if its not return false
    


"""
Previous attempt:

        
        while str == str:
            if s or t in str == str:
                return True
            else:
                return False


"""