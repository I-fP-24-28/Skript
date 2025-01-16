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
            return
            
        reference_node = self.root
        
        while reference_node:
            if reference_node.value > value and reference_node.left == None:
                node.parent = reference_node
                reference_node.left = node
                self.size += 1
                break
            elif reference_node.value > value:
                reference_node = reference_node.left
            elif reference_node.value < value and reference_node.right == None:
                node.parent = reference_node
                reference_node.right = node
                self.size += 1
                break
            else:
                reference_node = reference_node.right
            