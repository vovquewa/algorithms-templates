class StackNode:
    def __init__(self, value, prev=None, maximum=None):
        self.value = value
        self.prev = prev
        self.maximum = maximum

    def __str__(self) -> str:
        return f'{self.value} {self.prev} {self.maximum}'


class StackMax:
    def __init__(self):
        self.items = []

    def push(self, x):
        if self.items == []:
            x = StackNode(x, None, x)
        else:
            x = StackNode(
                x,
                self.items[-1],

                x if x > self.peek().maximum
                else self.peek().maximum
            )
        return self.items.append(x)

    def pop(self):
        if self.items == []:
            return print('error')
        return self.items.pop()

    def peek(self):
        if self.items == []:
            return print('None')
        return self.items[-1]

    def get_max(self):
        if self.items == []:
            return print('None')
        maximum = self.items[-1].maximum
        return print(maximum)

    def __str__(self) -> str:
        return f"{self.items}"


if __name__ == '__main__':

    stack = StackMax()
    n = int(input())

    for i in range(n):
        command = input()
        if command.split()[0] == 'push':
            stack.push(int(command.split()[1]))
        elif command.split()[0] == 'pop':
            stack.pop()
        elif command.split()[0] == 'get_max':
            stack.get_max()
        i += 1
