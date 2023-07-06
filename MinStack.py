class MinStack(object):

    def __init__(self):
        self.numlist = []
        self.minNum = []

    def push(self, val):
        self.numlist.append(val)

    def pop(self):
        self.numlist.pop()

    def top(self):
        return self.numlist[-1]

    def getMin(self):
        minNum = []
        for num in self.numlist:
            if minNum:
                if num < minNum[0]:
                    minNum[0] = num
            else:
                minNum.append(num)
        print(minNum)
        return minNum[0]

    # Not the most efficent but works
    def getMin(self):
        minNum = []
        for num in self.numlist:
            if minNum:
                if num < minNum[0]:
                    minNum[0] = num
            else:
                minNum.append(num)
        print(minNum)
        return minNum[0]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


stackTest = MinStack()
stackTest.push(-2)
stackTest.push(0)
stackTest.push(-3)
stackTest.pop()
stackTest.getMin()
