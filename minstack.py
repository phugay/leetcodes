# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack(object):

    def __init__(self):
        self.nums = []
        

    def push(self, x):
        self.nums.append(x)
        

    def pop(self):
        return self.nums.pop()
        

    def top(self):
        return self.nums[len(self.nums)-1]
        

    def getMin(self):
        return min(self.nums)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()