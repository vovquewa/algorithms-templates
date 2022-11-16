class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_size = n
        self.head = 0
        self.tail = 0
        self.q_size = 0

    def is_empty(self):
        return self.q_size == 0

    def push(self, x):
        if self.q_size != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.q_size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            print('None')
            return
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.q_size -= 1
        print(x)

    def peek(self):
        if self.is_empty():
            print('None')
            return
        print(self.queue[self.head])

    def size(self):
        print(self.q_size)

    def __str__(self) -> str:
        return f'{self.queue}'


count = int(input())
max_size = int(input())
q = MyQueueSized(max_size)
for i in range(count):
    lst_in = input().split()
    if lst_in[0] == 'push':
        q.push(int(lst_in[1]))
    elif lst_in[0] == 'pop':
        q.pop()
    elif lst_in[0] == 'peek':
        q.peek()
    elif lst_in[0] == 'size':
        q.size()