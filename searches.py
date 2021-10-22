from trees import Node
from q import Queue

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
I = Node('I')
J = Node('J')

A.left = B
A.right = C
B.left = D
B.right = E
E.left = H
C.left = F
C.right = G
G.left = I
G.right = J

def preorder(root):
    if root is not None:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.right)
        postorder(root.left)
        print(root.value)


# --------------------------

bfs_queue = Queue()

def BFS(node):
    global bfs_queue
    bfs_queue.add(node)

    while len(bfs_queue.q_list) != 0:
        item_to_remove = bfs_queue.remove()
        print(item_to_remove.value)

        if item_to_remove.left is not None:
            bfs_queue.add(item_to_remove.left)

        if item_to_remove.right is not None:
            bfs_queue.add(item_to_remove.right)
