class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(1)
b = Node(2)
c = Node(3)\
d = Node(4)
tail = d
e = Node(5)

def append_linked_list(node):
    # want e to come after the tail
    global tail
    tail.next = node
    node.next = None
    tail = node
    print(tail.value)
