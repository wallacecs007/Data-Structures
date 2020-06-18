"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    def push(self, value):

        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node

    def pop(self):

        if not self.head:
            return None

        if self.head.next_node is None:
            temp_value = self.head.value
            self.head = None
            self.tail = None
            return temp_value

        tail_value = self.head.value
        self.head = self.head.next_node
        return head_value
