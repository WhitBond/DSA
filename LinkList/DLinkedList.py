#
# DEDLinkedList.py - Double Ended Double Linked List implementation 
#
from DListNode import DListNode
class DEDLL(object):
    def __init__(self, Head = None, Tail=None):
        self._head = Head
        self._tail = Tail 
        self._count = 0
    
    def __len__(self):
        return self._count 

    def _isEmpty(self):
        return self._head == None

    def insertFirst(self, val):
        newNode = DListNode(val)
        if self._isEmpty():
            self._head = newNode
            self._tail = newNode 
            self._count += 1
        else:
            self._head.setPrev(newNode)
            newNode.setNext(self._head)
            self._head = newNode
            self._count += 1

    def insertLast(self, val):
        newNode = DListNode(val)
        if self._isEmpty():
            self._head = newNode
            self._tail = newNode
        else:
            self._tail.setNext(newNode)
            newNode.setPrev(self._tail)
            self._tail = newNode
        self._count += 1


    def delFirst(self):
        if self._isEmpty():
            raise Exception("Linked list is empty")
        else:
            retval = self._head
            self._head = self._head.getNext()
            retval.setNext(None)
            self._head.setPrev(None)
            self._count -= 1
        return retval

    def delLast(self):
        if self._isEmpty():
            raise Exception("Linked list os empty")
        else:
            retval = self._tail
            self._tail = self._tail.getPrev()
            self._tail.setNext(None)
            retval.setPrev(None)
            self._count -= 1
        return retval 

    def peekFirst(self):
        if self._isEmpty():
            raise Exception("Linked list is empty")
        return self._head 

    def peekLast(self):
        if self._isEmpty():
            raise Exception("Linked list is empty")
        return self._tail

    def printForward(self):
        if self._isEmpty():
            raise Exception("Linked list is empty")
        else:
            temp = self._head 
            while temp:
                print(temp, end = ' ')
                temp = temp.getNext()
            print()

    def printBackward(self):
        if self._isEmpty():
            raise Exception("Linked list is empty")
        else:
            temp = self._tail 
            while temp:
                print(temp, end= ' ')
                temp = temp.getPrev()
            print()
def main():
    linkedList = DEDLL()
    while True:
        print("\nLinked List Operations:")
        print("1. Insert First")
        print("2. Insert Last")
        print("3. Remove First")
        print("4. Remove Last")
        print("5. Display")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            value = input("Enter value to insert at the beginning: ")
            linkedList.insertFirst(value)
        elif choice == '2':
            value = input("Enter value to insert at the end: ")
            linkedList.insertLast(value)
        elif choice == '3':
            
            value = linkedList.delFirst()
            print("Removed value:", value)
            
        elif choice == '4':
            
            value = linkedList.delLast()
            print("Removed value:", value)
            
        elif choice == '5':
            print("Linked List:")
            linkedList.printForward()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()



