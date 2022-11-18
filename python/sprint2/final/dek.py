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


class Deque:
    def __init__(self, maximum: int):
        self.head = None
        self.tail = None
        self.maximum = maximum
        self.deque_size = 0

    def is_empty(self):
        return self.deque_size == 0

    def size(self):
        print(self.deque_size)
        return self.deque_size

    def push_back(self, value):
        if self.is_empty():
            node = Node(value)
            self.head = node
            self.tail = node
            self.deque_size += 1
        elif self.maximum == self.deque_size:
            print('error')
        else:
            node = Node(value)
            node_prev = get_node_by_index(self.head, self.deque_size - 1)
            node_prev.next = node
            self.tail = node
            self.deque_size += 1

    def push_front(self, value):
        if self.is_empty():
            node = Node(value)
            self.head = node
            self.tail = node
            self.deque_size += 1
        elif self.maximum == self.deque_size:
            print('error')
        else:
            node = Node(value)
            node.next = self.head
            self.head = node
            self.deque_size += 1

    def print_deque(self):
        if self.is_empty():
            print('None')
            return
        print('Очередь: ', end='')
        print_linked_list(self.head)
        print(f'Голова: {self.head.value}')
        print(f'Хвост: {self.tail.value}')
        print(f'Размер деки: {self.deque_size}')

    def pop_front(self):
        if self.is_empty():
            print('error')
            return
        h = self.head
        self.head = self.head.next
        self.deque_size -= 1
        print(h.value)
        return h

    def pop_back(self):
        if self.is_empty():
            print('error')
            return
        if self.deque_size == 1:
            t = self.tail
            self.head = None
            self.tail = None
            self.deque_size -= 1
            print(t.value)
            return t

        t = self.tail
        self.tail = get_node_by_index(self.head, self.deque_size - 2)
        self.tail.next = None
        self.deque_size -= 1
        print(t.value)
        return t

    def __str__(self):
        return f'{self.head.value}'


if __name__ == '__main__':

    # Тестовый прогон

    # q = Deque(4)
    # q.push_front(861)
    # q.push_front(-819)
    # q.pop_back()
    # q.print_deque()
    # q.pop_front()
    # q.print_deque()

    count = int(input())
    maximum = int(input())
    q = Deque(maximum)
    for i in range(count):
        lst_in = input().split()
        if lst_in[0] == 'push_front':
            q.push_front(int(lst_in[1]))
        elif lst_in[0] == 'push_back':
            q.push_back(int(lst_in[1]))
        elif lst_in[0] == 'pop_front':
            q.pop_front()
        elif lst_in[0] == 'pop_back':
            q.pop_back()
