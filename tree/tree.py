class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def preorder(self):
        print(self.value),
        if self.left: self.left.preorder()
        if self.right: self.right.preorder()

def invert(node):
    right = node.right
    left = node.left
    node.left = right
    node.right = left
    if (node.right):
        node.right = invert(node.right)
    if (node.left):
        node.left = invert(node.left)
    return node
    # Fill this in.
root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 

root.preorder()
# a b d e c f 
print("\n")
invert(root)
root.preorder()
# a c f b e d