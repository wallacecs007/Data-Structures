"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedQueue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next_node = new_node
            self.tail = new_node

        self.size += 1

    def dequeue(self):
        if not self.head:
            return None

        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            self.size = self.size - 1
            return head_value

        head_value = self.head.value
        self.head = self.head.next_node
        self.size = self.size - 1
        return head_value


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):

        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) == 0:
            return None

        value = self.storage.pop(0)
        return value
