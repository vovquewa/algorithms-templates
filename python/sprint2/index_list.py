class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next
    print("None")


def get_node_by_index(node, index):
    while index:
        node = node.next
        index -= 1
    return node


def insert_node(head, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next = head
        return new_node
    previous_node = get_node_by_index(head, index-1)
    new_node.next = previous_node.next
    previous_node.next = new_node
    return head


def delete_node(head, index):
    if index == 0:
        next_node = get_node_by_index(head, index+1)
        head = next_node
        return head
    previous_node = get_node_by_index(head, index-1)
    next_node = get_node_by_index(head, index+1)
    previous_node.next = next_node
    return head


def search_value(node, value):
    index = 0
    while node:
        if node.value == value:
            return index
        index += 1
        node = node.next
    return -1


# n3 = Node('third')
# n2 = Node('second', n3)
# n1 = Node('first', n2)


# node, index, value = n1, 0, 'new_node'
# print(get_node_by_index(node, 2).value)
# head = insert_node(node, index, value)
# head = delete_node(node, index, value)

# print_linked_list(node)

# print(search_value(node, 'first123'))


node3 = DoubleConnectedNode("node3")
node2 = DoubleConnectedNode("node2")
node1 = DoubleConnectedNode("node1")
node0 = DoubleConnectedNode("node0")

node0.next = node1

node1.prev = node0
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2



def last_node(node):
    # while node:
    #     if node.next:
    #         node = node.next
    #         continue
    #     return node
    while node:
        node.next, node.prev = node.prev, node.next
        node = node.prev
        # node = node.next

print(last_node(node0).value)