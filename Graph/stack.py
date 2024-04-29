import numpy as np

class Stack:
    def __init__(self, size = 10):
        self._top = -1
        self._size = size
        self._array = np.empty(self._size, dtype = object)

    #accessor function
    def isEmpty(self):
        return self._top == -1
    
    #accessor function
    def isFull(self):
        return self._top == self._size - 1
    
    #accessor function
    def size(self):
        return self._size

    #accessor function
    def count(self):
        return self._top + 1

    #mutator function
    def push(self, item):
        if self.isFull():
            print("Stack is full, unable to insert new value")
        else:
            self._top += 1
            self._array[self._top] = item

    #mutator function
    def pop(self):
        if self.isEmpty():
            item = "Stack is empty, nothing to pop"

        else:
            item = self._array[self._top]
            self._array[self._top] = None
            self._top -= 1
        return item

    #accessor function
    def top(self):
        if self.isEmpty():
            item = "Stack is empty, nothing at the top"
            return item

        else:
            return self._array[self._top]
    
    #accessor function
    def display(self):
        print(self._array)
