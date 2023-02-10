class ArrayStack:
    def __init__(self):
        self.data = []
    def size(self):
        return len(self.data)
    def is_empty(self):
        if len(self.data)==0:
            return True
        else:
            return False
    def push(self, getdt):
        self.data.append(getdt)
        return
    def pop(self):
        if self.is_empty():
            return "Underflow: Cannot pop data from an empty list"
        else:
            return self.data.pop()
    def stackTop(self):
        if self.is_empty():
            return None
        else:
            return self.data[-1]
    def printStack(self):
        print(self.data)

myStack = ArrayStack()
myStack.push(10);myStack.push(20);myStack.push(30)
myStack.printStack() 
x = myStack.pop()
print(x)
myStack.pop()
myStack.printStack()
myStack.pop()
print(myStack.is_empty())
print(myStack.pop())