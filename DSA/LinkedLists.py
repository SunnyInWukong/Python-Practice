#creating and interacting with linkedLists

import random

class Node:  # for the linked lists ( single or double)
    def __init__(self, element):  # Node constructor
        self.element = element
        self.next = self.prev = None  # None instead of null for whatever reason


# end of Node=======================================================================================
# ==================================================================================================

class SingleLinkedList:

    def __init__(self):
        self.head = None

    def append(self, element):  # adding links
        newNode = Node(element)
        if self.head is None:  # initializing the head node
            self.head = newNode
            return
        tail = self.head
        while tail.next:  # basically does while ( next exists) - returns false if .next = None
            tail = tail.next
        tail.next = newNode

    def printList(self):  # simple while loop print
        current = self.head
        while current:  # tests while(current != None)
            print(current.data, end=" ")
            current = current.next
        print()

    def printRecursive(self, Node):
        if Node is None:
            return
        print(Node.element, end=" | ")
        self.printRecursive(Node.next)

    def printRll(self):  # to use the recursive one
        self.printRecursive(self.head)
        print()


# single linked list testing
LL = SingleLinkedList()


# LL.append(1)
# LL.append(2)
# LL.append(3)
# LL.append("My, What A Bountiful Harvest You've Reaped!")
# while True: # quick user input to append the list - works
#     choice = int(input("do you want to: 1 - add an element to the list, or 2 - exit"))
#     if choice == 2:
#         break
#     LL.append(input("Enter The next element value"))
# LL.printRll()

# remove - sll's
# combine sll's
# reverse sll
# mergesort ( make 2 linkedLists, and mergesort them into one larger linkedList)
# quicksort singly LL
# bubblesort singly LL
# insertion sort sll

# end of SLL =======================================================================================
# ==================================================================================================

# class for Doubly Linked List
class DoubleLinkedList:  # double linked list
    def __init__(self):  # create class for objects to store the head & tail nodes
        self.head = self.tail = None

    def reverse(self):  # reverse dll
        head = self.head
        tail = self.tail
        current = head
        if head is None:  # if the head is empty
            print("empty")
        else:
            while current:  # flipping the pointers, no need to move any nodes
                current.next, current.prev = current.prev, current.next
                current = current.prev
            self.head, self.tail = self.tail, self.head  # visually less clear for me, but useful swapping strat
            # return head

    def append(self, element):  # append dll
        # fill in here
        new = Node(element)
        if self.head is None:
            self.head = self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new

    def removeElement(self, element):  # remove dll
        head = self.head
        if head is None:
            return "empty"
        else:
            while head:
                if head.element == element:
                    head.prev.next = head.next
                    head.next.prev = head.prev
                    break
                head = head.next

    def contain(self, element):
        if self.head is None:
            return False
        else:
            current = self.head
            while current:
                if current.element == element:
                    return True
                current = current.next
            return False  # when it doesn't have the specified element

    def RemovePosition(self, pos):
        head = self.head
        if head is None:
            return "empty"
        else:
            for i in range(pos):
                if head.next is None:
                    return "list is too small for that"
                head.prev.next = head.next
                head.next.prev = head.prev
                break

    def insertFirst(self, element):  # insert into dll
        head = self.head
        new = Node(element)
        if head is None:
            self.append(element)
        else:
            # new.prev = None
            new.next = head
            head.prev = new
            self.head = new

    def insertAt(self, pos, element):  # insertAt, pos starts at 0
        head = self.head
        new = Node(element)
        if head is None:
            self.append(element)
        else:
            if pos == 0:
                self.insertFirst(element)
            else:
                for i in range(pos):
                    if head.next is None:
                        return "list is too small for that"
                    head = head.next
                if (head is self.tail):
                    self.append(element)
                else:
                    prev = head.prev
                    new.next = head
                    new.prev = head.prev
                    prev.next = new
                    head.prev = new

    def right2Left(self):  # TraverseRight2Left
        tail = self.tail
        if tail is None:
            print("empty")
        else:
            current = tail
            a = []
            while (current.prev):
                a.append(current.element)
            return " ".join(a)

    def size(self):  # size
        head = self.head
        size = 0
        if head is None:
            return size
        else:
            current = head
            while (current):
                size += size
            return size

    # def combine(self, second):#combine dll's
    # fill in here

    def fill(self):  # to ease the testing a bit
        choice = int(input("do you want to 1: manually outline or 2: get testing one: "))
        if choice == 1:
            min1 = int(input("Enter the MIN size of the new DLL: "))
            max1 = int(input("Enter the MAX size of the new DLL: "))
            min2 = int(input("Enter the MIN possible # for the new DLL: "))
            max2 = int(input("Enter the MAX possible # for the new DLL: "))
            for i in range(random.randint(min2, max2)):  # create a DLL & print out its initial values
                self.append(random.randint(min2, max2))  # random, unordered
        else:  # being lazy here, no need for input validation
            for i in range(10):
                self.append(i)

    def print(self):  # print the DLL, to ease the testing a bit too
        head = self.head
        if head is None:
            return "empty"
        current = head
        print("")  # for the newline
        while current:
            print(current.element, end=" | ")
            current = current.next

    # read & fill from a file
    # write to a file

    def bubbleSort(self):  # bubblesort dll
        # fill in here
        head = self.head
        tail = self.tail
        if head is None:  # empty list
            return "empty"
        else:
            # sort by element values
            last = None
            swapped = True
            i = 0
            while swapped:  # outer while loop
                current = head
                swapped = False
                while current.next != last:  # inner while loop

                    if (current.element > current.next.element):  # bubble sort comparisons
                        data = current.element
                        current.element = current.next.element
                        current.next.element = data
                        swapped = True

                    current = current.next

                last = current
            return head

    # def quickSort(self): #quicksort dll
    # fill in here

    # def mergeSort(self): #mergesort dll
    # fill in here

    # def insertSort(self): #insertsort dll
    # fill in here


# testing out the DLL
k = DoubleLinkedList()
k.fill()
# k.bubbleSort()
# k.print()
# k.reverse()
# k.print()
# k.insertAt(0, 9999)
# k.insertFirst(8888)
k.print()


# end of DLL =======================================================================================
# ==================================================================================================