#
# DListNode - Double linked list node implementation 
#
class DListNode(object):
    """Double linked list node implementation 
    Attributes
        Data: The object type data, to store in node. Default value is none. 
        Prev: Pointer(address) to previous node in the list. Default value is none.
        Next: Pointer(address) to next node in the list. Default value is none.
    """
    def __init__(self, Data = None, Prev= None, Next=None):
        self._key = Data
        self._prev = Prev
        self._next = Next

    def __str__(self):
        """Dunder/Megical function to support printing the object
        Attributes:
            None
        """
        return str(self._key)

    def getKey(self):
        return self._key 

    def getNext(self):
        return self._next

    def getPrev(self):
        return self._prev 

    def setKey(self, item):
        self._key = item 

    def setNext(self,pointer):
        self._next = pointer

    def setPrev(self,pointer):
        self._prev = pointer
