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

class Node:  # for the single linked list
    def __init__(self, element, next):  # Node constructor
        self.element = element
        self.next = None


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
#LL.append("My, What A Bountiful Harvest You've Reaped!")
while True: # quick user input to append the list - works
    choice = int(input("do you want to: 1 - add an element to the list, or 2 - exit"))
    if choice == 2:
        break
    LL.append(input("Enter The next element value"))
LL.printRll()
