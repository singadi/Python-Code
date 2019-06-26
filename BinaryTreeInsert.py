# Binary Search Tree insert
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def treeOrder(root):
    if(root == None):
        return
    treeOrder(root.left)
    print(root.data, '')
    treeOrder(root.right)


def insert(root, key):
    if(root == None or root.data == None):
        return Node(key)
    
    if(key < root.data):
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    return root


keys = [15, 10, 20, 8, 12, 16, 25, 18 ]
root = Node(None)
for key in keys:
    root = insert(root, key)

treeOrder(root)