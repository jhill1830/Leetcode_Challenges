'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

'''
nums = [7, -9, 3, -6, 3, 5, 3, 6, -2, -5,
        8, 6, -4, -6, -4, -4, 5, -9, 2, 7, 0, 0]


def longestConsecutive(nums):
    sortArr = sorted(nums)
    compList = []
    consecList = []
    for val in sortArr:
        if len(consecList) == 0:
            consecList.append(val)
        if val-1 == consecList[len(consecList)-1]:
            consecList.append(val)
        if len(consecList) != 0 and len(compList) == 0 and val-1 > consecList[len(consecList)-1]:
            compList.append(val)
        if len(compList) != 0 and val-1 == compList[len(compList)-1]:
            compList.append(val)
        if len(compList) > 0 and val-1 > compList[len(compList)-1]:
            compList = [0]
            compList[0] = val
        if len(compList) > len(consecList):
            consecList = compList
            compList = []

    return len(consecList)
#    print(sortArr)


longestConsecutive(nums)
