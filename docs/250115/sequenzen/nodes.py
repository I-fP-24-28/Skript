# nodes.py

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return f'{super().__str__()}\nValue: {self.value}\nNext: {self.next}'
        
    def set_next(self, next):
        self.next = next
        
class BNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        
    def __str__(self):
        return f'{super().__str__()}\nParent: {self.parent}\nValue: {self.value}\nLinks: {self.left}\tRechts: {self.right}'