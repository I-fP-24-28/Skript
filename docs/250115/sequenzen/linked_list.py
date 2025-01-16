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
        
    def search(self, value):
        if self.start == None:
            return None
        
        node = self.start
        
        if node.value == value:
            return node
        
        while node.next:
            node = node.next
            if node.value == value:
                return node
            
        return None
    
    def delete(self, value):
        if self.start == None:
            return -1
        elif self.search(value) == None:
            return -1
        
        else:
            node = self.start
            if node.value == value:
                self.start = node.next
                return 0
            
            hook = node
            while node:
                if node.value == value:
                    hook.next = node.next
                    return 0
                hook = node
                node = node.next
                
            return -1