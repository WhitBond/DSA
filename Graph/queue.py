import numpy as np

class Queue:
    def __init__(self, size = 10):
        self._front = -1
        self._rear = -1
        self._size = size
        self._array = np.empty(self._size, dtype = object)

    #accessor function
    def isEmpty(self):
        return self._rear == -1 or self._front > self._rear

    #accessor function
    def isFull(self):
        return self._rear == self._size - 1

    #accessor function
    def front(self):
        if self.isEmpty():
            print("Queue is empty, nothing in front")
        else:
            return self._array[self._front]

    #accessor function
    def rear(self):
        if self.isEmpty():
            print("Queue is empty, nothing in rear")
        else:
            return self._array[self._rear]

    #accessor function
    def size(self):
        return self._size

    #mutator function
    def insert(self, item):
        if self.isFull():
            print("Queue is full, unable to insert")
        else:
            if self._rear == -1 or self._front == -1:
                self._rear = self._front = 0
                self._array[self._rear] = item
            else:
                self._rear += 1
                self._array[self._rear] = item

    #mutator function
    def remove(self):
        if self.isEmpty():
            print("Queue is empty, there is nothing to remove")
        else:
            item = self._array[self._front]
            self._front += 1
            return item

    #accessor function
    def count(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self._rear + 1 - self._front

    

