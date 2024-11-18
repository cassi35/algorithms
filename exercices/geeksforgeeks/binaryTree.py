class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self,data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            curr_node = self.root
            while True:
                if data < curr_node.data:
                    # Left
                    if curr_node.left == None:
                        curr_node.left = new_node
                        return 
                    else:
                        curr_node = curr_node.left
                elif data > curr_node.data:
                    # Right
                    if curr_node.right == None:
                        curr_node.right = new_node
                        return
                    else:
                        curr_node = curr_node.right

    def lookup(self,data):
        curr_node = self.root
        while curr_node:
            if curr_node.data == data:
                return True
            elif data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return False

    def print_tree(self):
        if self.root != None:
            self.printt(self.root)

    def printt(self,curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.data))
            self.printt(curr_node.right)

    def remove(self,data):
        if self.root == None:
            return False

        currentNode = self.root
        parentNode = None

        while currentNode:
            if data < currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.left
            elif data > currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.right
            elif data == currentNode.data:
                # Case 1: Node has no right child
                if currentNode.right == None:
                    if parentNode == None:
                        self.root = currentNode.left
                    else:
                        if data < parentNode.data:
                            parentNode.left = currentNode.left
                        elif data > parentNode.data:
                            parentNode.right = currentNode.left

                # Case 2: Node has a right child without a left child
                elif currentNode.right.left == None:
                    currentNode.right.left = currentNode.left
                    if parentNode == None:
                        self.root = currentNode.right
                    else:
                        if data < parentNode.data:
                            parentNode.left = currentNode.right
                        elif data > parentNode.data:
                            parentNode.right = currentNode.right

                # Case 3: Node has two children
                else:
                    # Find the smallest node in the right subtree (leftmost)
                    leftmost = currentNode.right
                    leftmostParent = currentNode.right
                    while leftmost.left != None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left
                    
                    # Replace current node with the leftmost node
                    if leftmostParent != currentNode.right:
                        leftmostParent.left = leftmost.right
                        leftmost.right = currentNode.right
                    leftmost.left = currentNode.left

                    if parentNode == None:
                        self.root = leftmost
                    else:
                        if data < parentNode.data:
                            parentNode.left = leftmost
                        elif data > parentNode.data:
                            parentNode.right = leftmost
                return True
        return False


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(8)
bst.remove(12)  # Should remove 12
x = bst.lookup(6)
print(x)  # True
y = bst.lookup(99)
print(y)  # False
bst.print_tree()  # Should print the tree without 12
# Python Program to Check if a Binary Tree is subtree
# of another binary tree

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Utility function to check if two trees are identical
def areIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    # Check if data and left/right subtrees are identical
    return (root1.data == root2.data and
            areIdentical(root1.left, root2.left) and
            areIdentical(root1.right, root2.right))

# Function to check if root2 is a subtree of root1
def isSubtree(root1, root2):
    if root2 is None:
        return True
    if root1 is None:
        return False

    # Check if the current node of root1 matches
    # the root of root2
    if areIdentical(root1, root2):
        return True

    # Recur for left and right subtrees of root1
    return isSubtree(root1.left, root2) or \
      isSubtree(root1.right, root2)

if __name__ == "__main__":
  
    # Construct Tree root1
    #          26
    #         /  \
    #        10   3
    #       / \    \
    #      4   6    3
    #       \
    #        30
    root1 = Node(26)
    root1.right = Node(3)
    root1.right.right = Node(3)
    root1.left = Node(10)
    root1.left.left = Node(4)
    root1.left.left.right = Node(30)
    root1.left.right = Node(6)

    # Construct Tree root2
    #          10
    #         /  \
    #        4    6
    #         \
    #          30
    root2 = Node(10)
    root2.right = Node(6)
    root2.left = Node(4)
    root2.left.right = Node(30)

    if isSubtree(root1, root2):
        print("true")
    else:
        print("false")
