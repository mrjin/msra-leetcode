class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        self.size = 0


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.size == 0:
            self.min.append(x)
        else:
            if x <= self.min[-1]:
                self.min.append(x)
        self.stack.append(x)
        self.size += 1
        

    def pop(self):
        """
        :rtype: void
        """
        tmp = self.stack.pop()
        self.size -= 1
        if tmp == self.min[-1]:
            self.min.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]