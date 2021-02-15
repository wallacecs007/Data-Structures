"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
                return
            new_node = BSTNode(value)
            self.left = new_node
        elif value >= self.value:
            if self.right is not None:
                self.right.insert(value)
                return
            new_node = BSTNode(value)
            self.right = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        found = False
        if self.value > target:
            if self.left is None:
                return False
            found = self.left.contains(target)
        if self.value <= target:
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        return self.value

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)
        fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left is not None:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right is not None:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = []
        queue.append(node)
        while len(queue) > 0:
            next_node = queue.pop(0)
            print(next_node.value)
            if next_node.left is not None:
                queue.append(next_node.left)
            if next_node.right is not None:
                queue.append(next_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        queue = []
        queue.append(node)
        while len(queue) > 0:
            next_node = queue.pop()
            print(next_node.value)
            if next_node.left is not None:
                queue.append(next_node.left)
            if next_node.right is not None:
                queue.append(next_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left is not None:
            self.left.pre_order_dft(self.left)
        if self.right is not None:
            self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left is not None:
            self.left.post_order_dft(self.left)
        if self.right is not None:
            self.right.post_order_dft(self.right)
        print(self.value)
