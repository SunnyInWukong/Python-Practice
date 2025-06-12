# simple binary search algorithm practice ( searching though a ordered array of user defined size)
import random


def binarySearch(low, high, target, array):  # assuming an ordered array of integers
    mid = int((low + high) / 2)
    if low > high:
        print("the array isn't in order")
    elif array[mid] == target:
        return True
    elif target > array[mid]:
        print("a")
        return binarySearch(mid + 1, high, target, array)
    elif target < array[mid]:
        # print("b")
        return binarySearch(low, mid - 1, target, array)
    elif low == high:
        return False  # the item isnt present in the array


# #defining a simple ordered array to search through
# n = int(input("enter the size of the array to use"))
# arr = []
# for i in range(n):  # need to use range() to make it work like a normal for loop
#     arr.append(i)
#    # print(arr[i])
# goal = int(input("define the value you want to determine is present in the array")) # getting the target value
# print(binarySearch(arr[0], arr[len(arr)-1], goal, arr)) #test implementation - it worked

class Node:  # for the linked lists ( single or double)
    def __init__(self, element):  # Node constructor
        self.element = element
        self.next = self.prev = None  # None instead of null for whatever reason


class SingleLinkedList:

    def __init__(self):
        self.head = None

    def append(self, element):  # adding links
        newNode = Node(element, None)
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

    # def reverse(self): #reverse dll
    # fill in here

    def append(self, element):  # append dll
        # fill in here
        new = Node(element)
        if self.head is None:
            self.head = self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new

    # def remove(self):#remove dll
    # fill in here

    # def insertFirst(self,element):#insert into dll
    # fill in here

    # def combine(self, second):#combine dll's
    # fill in here

    def bubbleSort(self):  # bubblesort dll
        # fill in here
        head = self.head
        tail = self.tail
        if head is None:  # empty list
            return
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
for i in range(10):  # create a DLL & print out its initial values
    k.append(random.randint(0, 20))  # random, unordered
    # k.append(10-i) # reverse order
    # print(k.head.element, end="| ")
    # print(k.tail.element)
    print(k.tail.element, end="| ")

print("")
current = k.bubbleSort()
for n in range(10):
    print(current.element, end="| ")
    current = current.next

# end of DLL =======================================================================================
# ==================================================================================================
# look into cuda cones for ML, parallel processing, and the linear algebra behind the node tuning for ML
