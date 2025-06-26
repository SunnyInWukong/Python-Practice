# binary tree practice

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

    def levelOrderTraversal(self, tn):  # print the level order traversal of the tree
        # simple 'tree traversal using queues' pracice here
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

