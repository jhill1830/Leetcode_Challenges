class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int

There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.



Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Example 2:

Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.

Example 3:

Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.

        if len(position) == 1: return 1
        if pos + speed of ith car >= pos + speed of ith+1 car: 1 fleet

        have to keep track of each fleet and its speed

        may have to iterate through the target and move each car for each speed and then pop off the car that is going faster. The cars position would change each iteration.  Once target has been reached pop off the fleet and count it
        """
        if len(position) == 1:  # only one fleet if there's only one car
            return 1

        answer = 0
        fleet = [0] * len(position)  # position, speed
        for i, car in enumerate(position):
            fleet[i] = [car, speed[i]]
        fleet.sort()
        fleet.reverse()

        for move in range(target):
            i = 0
            j = 0
            for i in range(len(fleet)):
                if j != i:
                    i = j
                if fleet[i][0] < target:
                    fleet[i][0] += fleet[i][1]
                if i > 0 and fleet[i][0] >= fleet[i-1][0]:
                    fleet.pop(i)
                    j -= 1
                j += 1

            while fleet and fleet[0][0] >= target:
                fleet.pop(0)
                answer += 1
            if not fleet:
                return answer

        return


test = Solution()
# print(test.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
print(test.carFleet(31, [5, 26, 18, 25, 29, 21, 22,
      2, 19, 6], [7, 6, 6, 4, 3, 4, 9, 7, 6, 4]))
