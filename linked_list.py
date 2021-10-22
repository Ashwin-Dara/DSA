class NodeList:
    def __init__(self, value):
        self.value = value
        self.next = None

head = NodeList(10)
bead = NodeList(20)
cead = NodeList(30)

head.next = bead
bead.next = cead
cead.next = None

def traverse_list(head_node):
    current_node = head_node
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


bhalfead = NodeList(25)

# the node needs to be global
def insert_node(target_value, head_node, inserted_node):
    current_node = head_node
    while current_node is not None:
        if current_node.value == target_value:
            current_node.next, inserted_node.next = inserted_node, current_node.next
            return
        current_node = current_node.next


def remove_node(value, head):
    current_node = head
    while current_node is not None:
        if current_node.next.value == value:
                current_node.next = current_node.next.next
                return None
        current_node = current_node.next
