class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

a = Node(72)
b = Node(61)
c = Node(90)
d = Node(54)
e = Node(104)
f = Node(82)
g = Node(92)

a.right = c
a.left = b
b.left = d
b.right = e
c.left = f
c.right = g

def find_node(node, value):
    if node is None:
        print("Node was not found")
        return
    if node.value == value:
        print("Node was found")
    if value > node.value:
        find_node(node.right, value)
    if value < node.value:
        find_node(node.left, value)

def insert_node(node, new_node):
    if node.right == None and new_node.value > node.value:
        node.right = new_node
    elif node.left == None and new_node.value < node.value :
        node.left = new_node
    if node is not None and new_node.value > node.value:
        insert_node(node.right, new_node)
    if node is not None and new_node.value < node.value:
        insert_node(node.left, new_node)
