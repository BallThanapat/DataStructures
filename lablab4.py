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

# def matching(exp):
#     stack = ArrayStack()
#     for i in exp:
#         if i == "(":
#             stack.push(i)
#         elif i == ")":
#             if stack.is_empty():
#                 return False
#             else:
#                 stack.pop()
#     if stack.is_empty():
#         return True
#     else:
#         return False

# x = matching("((((A+B)*C))))")
# print(x)

# stack1 = ArrayStack();stack2 = ArrayStack()
# stack1.push(10);stack1.push(20);stack1.push(30)
# stack2.push(15);stack2.push(30)
# stack1.printStack();stack2.printStack()

# def copyStack(stack1,stack2):
#     tmp = ArrayStack()
#     while stack2.is_empty() == False:
#         stack2.pop()
#     while stack1.is_empty() == False:
#         x = stack1.pop()
#         tmp.push(x)
#     tmp.printStack()
#     while not tmp.is_empty():
#         x = tmp.pop()
#         stack1.push(x)
#         stack2.push(x)
#     stack1.printStack()
#     stack2.printStack()
# copyStack(stack1, stack2)

def infixToPostfix(exp):
    stack = ArrayStack()
    res = ""
    thisdict =	{"+": 1,"-": 1,"*": 2,"/": 2}
    for i in exp:
        if i not in thisdict:
            res += i
        else:
            if stack.is_empty():
                stack.push(i)
            else:
                if thisdict[i] > thisdict[stack.stackTop()]:
                    stack.push(i)
                else:
                    while not stack.is_empty():
                        res += stack.pop()
                        if stack.is_empty() or thisdict[i] > thisdict[stack.stackTop()]:
                            stack.push(i)
                            break
    while not stack.is_empty():
        res += stack.pop()
    return res
exp = "A+B*C/D-E"
x = infixToPostfix("A+B*C/D-E")
print("Postfix of",exp,"is",x)
