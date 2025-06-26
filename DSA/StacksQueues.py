#Self built Stacks and Queues using self made linkedlists

from practice.DSA.LinkedLists import DoubleLinkedList

class LinkedStack:
    def __init__(self):
        self.dll = DoubleLinkedList()  # independent instance of the dll instead of inheriting from it

    def pop(self):
        value = self.dll.tail.element  # store the value for the return
        self.dll.RemovePosition(self.dll.size)  # should remove the last element, replaces the tail value
        return value  # returns the value that was removed

    def push(self, element):
        self.dll.append(element)  # adds a value to the back of the list ( top of the stack)

    def peak(self):
        return self.dll.tail.element  # returns the value at the end of the list / top of the stack

    def isEmpty(self):
        return self.dll.size() == 0  # boolean return for if its empty

    def size(self):
        return self.dll.size()  # return the size of the stack


# end of LinkedStack ===============================================================================
# ==================================================================================================

class LinkedQueue:  # basically the same as the stack but using head instead of tail
    def __init__(self):
        self.dll = DoubleLinkedList()  # independent instance of the dll instead of inheriting from it

    def pop(self):
        value = self.dll.head.element  # store the value for the return
        self.dll.RemovePosition(0)  # should remove the first element, replaces the head value
        return value  # returns the value that was removed

    def push(self, element):
        self.dll.insertFirst(element)  # remove the head of the list / next value in queue

    def peak(self):
        return self.dll.head.element  # returns the value at the head of the list / next in the queue

    def isEmpty(self):
        return self.dll.size() == 0  # boolean return for if its empty

    def size(self):
        return self.dll.size()  # return the size of the stack


# end of LinkedQueue ===============================================================================
# ==================================================================================================
