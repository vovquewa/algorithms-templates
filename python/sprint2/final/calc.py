# Посылка 75246991
class Node:
    """Односвязный список"""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def _print_linked_list(vertex):
    """Печать односвязной последовательности"""
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next
    print("None")


class Stack:
    """
    Реализация калькулятора. Обработка польской нотации.

    # Тестовый прогон #1
    # stack = Stack()
    # stack.calculation(10)
    # stack.calculation(20)
    # stack.calculation(25)
    # stack.calculation(24)
    # stack.calculation('+')
    # stack._print_stack()
    # stack.calculation('+')
    # stack._print_stack()
    # stack.calculation('/')
    # stack.print_head()

    # Тестовый прогон #2 (2 5 - 4 /)
    # print('Тестовый прогон 2')
    # stack = Stack()
    # stack.calculation(2)
    # stack.calculation(5)
    # stack._print_stack()
    # stack.calculation('-')
    # stack._print_stack()
    # stack.calculation(4)
    # stack._print_stack()
    # stack.calculation('/')
    # stack._print_stack()

    # Тестовый прогон #3 (4 13 5 / +) Результат 6
    # print('Тестовый прогон 3')
    # stack = Stack()
    # stack.calculation(4)
    # stack.calculation(13)
    # stack.calculation(5)
    # stack._print_stack()
    # stack.calculation('/')
    # stack._print_stack()
    # stack.calculation('+')
    # stack._print_stack()

    """
    def __init__(self):
        self._head = None
        self._stack_size = 0

    def _is_empty(self):
        return self._stack_size == 0

    def _push_forward(self, value):
        if self._is_empty():
            node = Node(value)
            self._head = node
            self._stack_size += 1
            return node
        next = self._head
        node = Node(value, next)
        self._head = node
        self._stack_size += 1
        return node

    def _print_stack(self):
        if self._is_empty():
            print('None')
            return
        print('Очередь: ', end='')
        _print_linked_list(self._head)
        print(f'Голова: {self._head.value}')
        print(f'Размер: {self._stack_size}')

    def calculation(self, value):
        operations = ['-', '+', '*', '/']
        if value in operations:
            b = self._head
            a = self._head.next
            self._head = self._head.next.next
            self._stack_size -= 2
            if value == '+':
                result = a.value + b.value
                self._push_forward(int(result))
                return
            if value == '-':
                result = a.value - b.value
                self._push_forward(int(result))
                return
            if value == '*':
                result = a.value * b.value
                self._push_forward(int(result))
                return
            if value == '/':
                result = int(a.value // b.value)
                self._push_forward(int(result))
                return
        self._push_forward(int(value))

    def print_head(self):
        print(self._head.value)


if __name__ == '__main__':

    stack = Stack()
    lst_inp = input().split()
    for item in lst_inp:
        stack.calculation(item)
    stack.print_head()
