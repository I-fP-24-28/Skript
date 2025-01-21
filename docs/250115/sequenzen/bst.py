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
        if self.root is None:
            self.root = node
            self.size += 1
            return
            
        reference_node = self.root
        
        while reference_node:
            if reference_node.value > value and reference_node.left is None:
                node.parent = reference_node
                reference_node.left = node
                self.size += 1
                break
            elif reference_node.value > value:
                reference_node = reference_node.left
            elif reference_node.value < value and reference_node.right is None:
                node.parent = reference_node
                reference_node.right = node
                self.size += 1
                break
            else:
                reference_node = reference_node.right
                
    def search(self, value):
        if self.root is None:
            return -1
        
        if self.root.value == value:
            return self.root
        
        reference_node = self.root
                
        while reference_node:
            if reference_node.value == value:
                return reference_node
            elif reference_node.value > value and reference_node.left is None:
                return -1
            elif reference_node.value > value:
                reference_node = reference_node.left
            elif reference_node.value < value and reference_node.right is None:
                return -1
            else:
                reference_node = reference_node.right
                
    def traversal(self):
        result = []
        stack = []
        current = self.root

        while current is not None or stack:
            # Gehe so weit wie möglich nach links und speichere die Knoten im Stack
            while current is not None:
                stack.append(current)
                current = current.left
            
            # Der letzte Knoten im Stack ist der nächste Knoten, den wir besuchen
            current = stack.pop()
            result.append(current)  # Verarbeite den aktuellen Knoten
            
            # Gehe zum rechten Teilbaum
            current = current.right

        return result  # Gib das Ergebnis zurück
                
    def delete(self, value):
        node = self.search(value)
        
        # leaf
        if node.left is None and node.right is None:
            if node.parent.value > value:
                node.parent.left = None
            else:
                node.parent.right = None
                
        # one child left
        elif node.left is not None and node.right is None:
            parent = node.parent
            child = node.left
            parent.left = child
            child.parent = parent
            node.parent = None
            node.left = None
            
        # one child right
        elif node.right is not None and node.left is None:
            parent = node.parent
            child = node.left
            parent.right = child
            node.parent = None
            node.let = None