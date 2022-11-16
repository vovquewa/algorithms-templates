class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def get_node_by_index(node, index):
    while index:
        node = node.next
        index -= 1
    return node


def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next
    print("None")


class ListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.q_size = 0

    def is_empty(self):
        return self.q_size == 0

    def size(self):
        print(self.q_size)
        return self.q_size

    def put(self, value):
        if self.is_empty():
            node = Node(value)
            self.head = node
            self.q_size += 1
        else:
            node = Node(value)
            node_prev = get_node_by_index(self.head, self.q_size - 1)
            node_prev.next = node
            self.tail = node
            self.q_size += 1

    def print_queue(self):
        print_linked_list(self.head)

    def get(self):
        if self.is_empty():
            print('error')
            return
        h = self.head
        self.head = self.head.next
        self.q_size -= 1
        print(h.value)
        return h

    def __str__(self):
        return f'{self.head.value}'


q = ListQueue()

# q.put(5)
# q.put(1)
# q.put(6)
# q.print_queue()
# q.size()
# q.get()
# q.size
# q.get()
# q.get()
# q.print_queue()

count = int(input())
for i in range(count):
    lst_in = input().split()
    if lst_in[0] == 'put':
        q.put(int(lst_in[1]))
    elif lst_in[0] == 'get':
        q.get()
    elif lst_in[0] == 'size':
        q.size()
