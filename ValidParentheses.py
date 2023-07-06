'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''

s = "()()"


def isValid(s: str) -> bool:
    if s[0] == "}" or s[0] == "]" or s[0] == ")":  # check if starting with opening parenthesee
        return False

    stack = []
    matchedDict = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in matchedDict:
            if stack and stack[-1] == matchedDict[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return True if not stack else False


isValid(s)
