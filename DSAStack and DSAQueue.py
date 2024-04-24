#
#
#
import numpy as np
defau_capacity=100
class DSAStack:
    def __init__(self, capacity= None) :
        if capacity is None:

            self.capacity =defau_capacity
        else:
            self.capacity=capacity
        self._arr =np.empty(self.capacity,dtype =object)
        self.count=0
    def get_count(self):
        return self.count
    def is_empty(self):
        return self.count == 0
    def is_full(self):
        return self.count == len(self._arr)
    def push(self,item):
        if self.is_full():
            raise IndexError("Stack is full")
        self._arr[self.count] = item
        self.count+=1
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        item=self._arr[self.count -1]
        self.count-=1
        return item
    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._arr[self.count-1]
    
class DSAQueue:
    def __init__(self, capacity= None) :
        if capacity is None:

            self.capacity =defau_capacity
        else:
            self.capacity=capacity
        self._arr =np.empty(self.capacity,dtype =object)
        self.rear=-1
        self.front=0
        self.count =0
    def get_count(self):
        return self.count
    def is_empty(self):
        return self.count == 0
    def is_full(self):
        return self.count == len(self._arr)
    def enqueue(self,item):
        if self.is_full():
            raise IndexError("Quee is full")
        self.rear+=1
        self._arr[self.rear] = item
        self.count+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Que is empty")
        else:
            print("the item is removed is ",self._arr[self._front])
            self.front+=1
            self.count-=1
class CircularQueue(DSAQueue): #implement Cir
    def __init__(self,capacity):
        super().__init__(capacity)
        self._front=-1
        self._rear=-1
    def enqueue(self,item):
        if self._rear - self._front == self.capacity -1 or self._front -self._rear==1:
            raise Exception("CQueue is full")
        elif (self._front ==-1):
            self._front =0
            self._rear=0
            self._arr[self._rear]=item
        else:
            self._rear =(self._rear+1)%self.capacity
            self._arr[self._rear]=item
            print("the item is add is",item)
    def dequeue(self):
        if self._front ==-1:
            raise Exception("CQueue is empty")
        else:
            if self._front==self._rear:
                delete=self._arr[self._front]
                self._front=-1
                self._rear=-1
                print("the item is added is",delete)
            else:
                delete =self._arr[self._front]
                self._front=(self._front+1) % self.capacity
                print("the item is remove is",delete)
class Shuffling(DSAQueue):
    def __init__(self,capacity):
        super().__init__(capacity)
        self.front=0
        self.rear=-1
    def enqueue(self,item):
        super().enqueue(item)
    def dequeue(self):
        super().dequeue()
    def shuffingQueue(self):
        item=self._arr[0]
        for i in range(self.count):
            self._arr[i]=self._arr[i+1]
        return item

