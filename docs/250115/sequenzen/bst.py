# bst.py

from nodes import BNode

class BST:
    def __init__(self, root_value=None):
        if root_value:
            node = BNode(root_value)
            self.root = node
            self.size = 1
        else:
            self.root = None
            self.size = 0
            
    def append(self, value):
        node = BNode(value)
        if self.root == None:
            self.root == node
            self.size += 1