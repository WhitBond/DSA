#
#
#
from DListNode import DListNode
from DLinkedList import DEDLL
import numpy as np
class DSAStack:
    def __init__(self) :
        self.stacklist=DEDLL()
    def get_count(self):
        return self.count
    def is_empty(self):
        self.stacklist._isEmpty()
    def push(self,item):
        self.stacklist.insertFirst()
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stacklist.delFirst()
    def top(self):
        self.stacklist.peekFirst()
class DSAQueue():
    def __init__(self) :
        self.stacklist = DEDLL()
    def get_count(self):
        return self.count
    def is_empty(self):
        self.stacklist._isEmpty()
    def enqueue(self,item):
        self.stacklist.insertLast(item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.stacklist.delFirst()
