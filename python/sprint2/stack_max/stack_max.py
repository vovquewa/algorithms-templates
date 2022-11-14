class StackMax:
    def __init__(self):
        self.items = []

    def push(self, x):
        return self.items.append(x)

    def pop(self):
        if self.items == []:
            return print('error')
        return self.items.pop()

    def get_max(self):
        if self.items == []:
            return print('None')
        maximum = max(self.items)
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
