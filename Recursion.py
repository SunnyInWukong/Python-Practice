# My main file for practicing OOP & DSA in python
# I made classes for:Nodes, TreeNodes, singleLinkedLists, DoubleLinkedLists, Stacks, Queues, Binary Tree
import random


# simple binary search algorithm practice ( searching though a ordered array of user defined size)
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

# end of array searching algorithms ================================================================
# ==================================================================================================

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

# look into cuda cones for ML, parallel processing, and the linear algebra behind the node tuning for ML
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

class TreeNode:
    def __init__(self, element):
        self.left = self.right = self.parent = None  # added for Trees
        self.element = element


# end of TreeNode ==================================================================================
# ==================================================================================================

# review and add methods to this to practice recursion.
class BinaryTree:  # had to create seperately from the DLL and SLL
    def __init__(self):
        self.root = self.leaf = None
        self.tn = TreeNode  # will have to do tn = self.tn for every method b/c python doesnt seem to have global variables

    def addChildToNode(self, element, target):  # add a node after the specified element, left -> right priority
        tn = self.tn(element)
        node = self.findNode(target)
        if (self.root is None):
            return "The Tree Is Empty"
        if (node is None):  # not present in the list
            print("No Such Element Present In the Tree")
        if node.left is None:
            node.left = tn
        if node.right is None:
            node.right = tn
        else:
            print("Both Child Nodes Are Already Assigned To The Specified Element")

    def findNode(self, element):  # returns the specific node
        return self.nodeFinder(element, self.root)  # implement the nodefinder method starting from the root

    def nodeFinder(self, element, tn):  # recursively go through the tree & check if it's present & return it if it is
        if tn is None:  # if the node is null, stop & return that thread is null
            return None
        if tn.element == element:  # if the node is found, return that node
            return tn
        left = self.nodeFinder(element, tn.left)  # traversing the left branch of the node
        if left:
            return left  # if found in the left branch, return the element in that branches return
        return self.nodeFinder(element, tn.right)  # if not found in the left, check the right

    def size(self):  # return number of nodes
        return self.countNodes(self.root)

    def countNodes(self, tn):  # recursively go through the tree & count the nodes
        if tn is None:
            return 0
        return 1 + self.countNodes(tn.left) + self.countNodes(tn.right)

    def height(self):
        return self.findHeight(self.root)

    def findHeight(self, tn):  # depth of the tree
        if (self.root is None):  # empty tree
            return 0
        if (tn is None):  # if this branch is empty
            return 0
        left = self.findHeight(tn.left)  # go through the left branches
        right = self.findHeight(tn.right)  # go through the right branches
        return 1 + max(left, right)  # return 1 + depth so far & compare which side is longer

    def depth(self, element):  # find the depth of a node with a given element
        result = self.findDepth(element, self.root, 0)
        if (result == -1):
            return "No Node With Such Element Present In The Tree"
        if (result is None):
            return "the tree is empty"
        return result

    def findDepth(self, target, tn, depth):
        if self.root is None:  # if the tree is empty
            return None
        if tn is None:  # if the node traversed to is empty
            return -1  # returns a non-valid depth
        if (tn == target):  # if the node is found
            return depth
        left = self.findDepth(target, tn.left, depth + 1)
        right = self.findDepth(target, tn.right, depth + 1)
        if left != -1:  # if the left isnt empty, return it
            return left
        return right  # if the left is empty, return the right

    def addRoot(self, element):  # add root
        if (self.root is None):
            node = self.tn(element)
            self.root = node
            return
        print("There is Already a Root Node")

    def numTreeFromFile(self, fileName):  # build a numeric binary tree from numbers in a .csv file
        a = 10
        # parse through a .csv file, with the tree values, and make a sorted binary tree

    def kpTreeFromFile(self, fileName):  # build a key-value binary tree from values in a file
        # might want to create a record class for the key/value pair instead of editing the treenode class
        a = 10
    def levelOrderTraversal(self, tn): # print the level order traversal of the tree
        #simple 'tree traversal using queues' pracice here
        a = 10

    # create ordered tree with specified number of nodes (left to right 1 - 2, 3. 2- 4, 5. 3 - 6, 7. etc.
    # delete a node
    # replace a node
    # print out (left to right, depth first)
    # print out (left to right, breadth first)
    # sort (largest on top)

# end of BinaryTree ================================================================================
# ==================================================================================================


# to-do :
# Array work
# tree traversal
# depth of a node
# height of a tree
# trie
# adjacent list /adjacent matrix
# making a class in another file to import to in this one, maybe for expanding the element in the nodes or something
# Key value binary tree
# searching through numeric binary search trees & non-numeric ones to find specified nodes
# red/black binary tree
# printing out binary trees wih queues
# printing binary trees recursively ( in different orders)
# practice methods for using the "parent" pointer in a tree node class to find common ancestors and such
# hash tables
# priority queue : basically have another element for priority in the node to sort the queue by

