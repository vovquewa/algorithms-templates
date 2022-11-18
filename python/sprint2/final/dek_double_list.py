# Посылка 75246488
class Node:
    """Класс двусвязной последовательности"""

    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def _print_linked_list(vertex):
    """Печать двусвязной последовательности"""
    print("None", end=' <--> ')
    while vertex:
        print(vertex.value, end=' <--> ')
        vertex = vertex.next
    print("None")


class Deque:
    """
    Структура данных Дек, максимальный размер которого определяется заданным
    числом.

    Методы:
    - push_back(x) добавление элемента в конец дека
    - push_front(x) добавление элемента в начало дека
    - pop_back() удаление крайнего элемента дека
    - pop_front() удаление первого элемента дека

    Сложность работы алгоритма определяется как O(1)

    Отладка:
    q = Deque(4)
    q.push_front(861)
    q.push_front(-819)
    q.pop_back()
    q._print_deque()
    q.pop_front()
    q._print_deque()

    """

    def __init__(self, maximum: int):
        self._head = None
        self._tail = None
        self.maximum = maximum
        self._deque_size = 0

    def is_empty(self):
        return self._deque_size == 0

    def size(self):
        print(self._deque_size)
        return self._deque_size

    def push_back(self, value):
        if self.is_empty():
            node = Node(value)
            self._head = node
            self._tail = node
            self._deque_size += 1
        elif self.maximum == self._deque_size:
            raise OverflowError
        else:
            node = Node(value)
            node_prev = self._tail
            node.prev = self._tail
            node_prev.next = node
            self._tail = node
            self._deque_size += 1

    def push_front(self, value):
        if self.is_empty():
            node = Node(value)
            self._head = node
            self._tail = node
            self._deque_size += 1
        elif self.maximum == self._deque_size:
            raise OverflowError
        else:
            node = Node(value)
            node.next = self._head
            node_next = self._head
            node_next.prev = node

            self._head = node
            self._deque_size += 1

    def _print_deque(self):
        if self.is_empty():
            print('None')
            return
        print('Очередь: ', end='')
        _print_linked_list(self._head)
        print(f'Голова: {self._head.value}')
        print(f'Хвост: {self._tail.value}')
        print(f'Размер деки: {self._deque_size}')

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        h = self._head
        self._head = self._head.next
        self._deque_size -= 1
        print(h.value)
        return h

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        if self._deque_size == 1:
            t = self._tail
            self._head = None
            self._tail = None
            self._deque_size -= 1
            print(t.value)
            return t

        t = self._tail
        tail_prev = self._tail.prev
        self._tail = tail_prev
        self._tail.next = None
        self._deque_size -= 1
        print(t.value)
        return t

    def __str__(self):
        return f'{self._head.value}'


if __name__ == '__main__':

    count = int(input())
    maximum = int(input())
    q = Deque(maximum)
    for i in range(count):
        lst_in = input().split()
        if lst_in[0] == 'push_front':
            try:
                q.push_front(int(lst_in[1]))
            except OverflowError:
                print('error')
        elif lst_in[0] == 'push_back':
            try:
                q.push_back(int(lst_in[1]))
            except OverflowError:
                print('error')
        elif lst_in[0] == 'pop_front':
            try:
                q.pop_front()
            except IndexError:
                print('error')
        elif lst_in[0] == 'pop_back':
            try:
                q.pop_back()
            except IndexError:
                print('error')
