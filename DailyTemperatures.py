
def dailyTemperatures(temperatures):
    """
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

    """

# needs to wait to find day warmer than current day. Only if either finding a warmer day or getting to the end of the list (return 0) will it iterate to next day.
# store current warmest day

# using monotonic stack technique.  IE. each succeeding stack element will be less than previous

    # create array of the length of input length
    answer = [0] * len(temperatures)
    stack = []

    # iterate through list of day temps
    for ind, day in enumerate(temperatures):
        # while the stack isn't empty and the current day temp is greater than the previous stack day temp
        while stack and day > stack[-1][0]:
            stackT, stackInd = stack.pop()  # store the previous days index and temp
            # use the difference between current iteration and the popped stack index to find number of days.  Input this result into the popped stack index position
            answer[stackInd] = ind-stackInd

        # add the day temp and its index position to stack
        stack.append([day, ind])
    return answer

# # works, but slow. 0(n2)
#     answer = []
#
#     for i, today in enumerate(temperatures):
#         count = 0
#         for j, nextDay in enumerate(temperatures[i+1:]):
#             if nextDay > today:
#                 count += 1
#                 answer.append(count)
#                 break
#             if i + j + 2 == len(temperatures):
#                 answer.append(0)
#                 break
#             else:
#                 count += 1
#     answer.append(0)
#
#     return answer


dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
