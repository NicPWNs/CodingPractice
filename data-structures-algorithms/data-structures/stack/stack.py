#!/usr/bin/env python3

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return  self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

if __name__ == '__main__':

    s = Stack()

    print("Is the stack empty?: " + str(s.is_empty()))

    print("Pushing a '1' onto the stack.")
    s.push(1)
    print("Pushing a '2' onto the stack.")
    s.push(2)
    print("Pushing a '3' onto the stack.")
    s.push(3)
    print("Pushing a '4' onto the stack.")
    s.push(4)
    print("Pushing a '5' onto the stack.")
    s.push(5)

    print("Item at top of the stack is: " + str(s.peek()))

    print("Popping top item from the stack.")
    s.pop()

    print("Item at top of the stack is: " + str(s.peek()))

    print("Is the stack empty?: " + str(s.is_empty()))

    print("How big is the stack?: " + str(s.size()))