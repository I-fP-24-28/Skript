# linked_list.py

from nodes import Node

class LinkedList:
    def __init__(self, value=None):
        self.length = 0
        if value:
            node = Node(value)
            self.start = node
            self.length += 1
        else:
            self.start = None
            
    def append(self, value):
        node = Node(value)
        node.next = self.start
        self.start = node