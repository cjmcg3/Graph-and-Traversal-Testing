class Stack:
    #constructor
    def __init__(self):
        self.__stack = []  # create private stack
    #methods
    def pop(self):  #pop the item
        if self.isEmpty(): return None
        return self.__stack.pop()

    def peek(self): #peek the item (no removal)
        if self.isEmpty(): return None
        return self.__stack[len(self.__stack)-1]

    def push(self, item): #push the item
        self.__stack.append(item)

    def size(self):           #return stack size
        return len(self.__stack)

    def isEmpty(self):           #return stack size
        return self.size()==0
