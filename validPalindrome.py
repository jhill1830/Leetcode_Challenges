import re


class Solution(object):
    def isPalindrome(self, s):
        """
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


        """
        regex = re.compile('[a-zA-Z0-9]')
        chars = regex.findall(s.lower())

        if not chars or len(chars) == 1:
            return True

        for i in range(len(chars)):
            if i < len(chars)/2:
                if chars[i] != chars[len(chars)-i-1]:
                    return False
            else:
                return True

        # regex or for loop to remove any non alphanumeric characters(eg ',.!: etc) elements in string

        # if first and last index, iterating to the middle != the same value. return False


test = Solution()
print(test.isPalindrome("f__"))
