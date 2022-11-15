# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, x):
#         return self.items.append(x)

#     def pop(self):
#         if self.items == []:
#             return print('error')
#         return self.items.pop()

#     def get_max(self):
#         if self.items == []:
#             return print('None')
#         maximum = max(self.items)
#         return print(maximum)

#     def peek(self):
#         if self.items == []:
#             return print('None')
#         return self.items[-1]

#     def __str__(self) -> str:
#         return f"{self.items}"


# if __name__ == '__main__':
lst_inp = list(input())


def is_correct_bracket_seq(lst_inp):
    class Stack:
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

        def peek(self):
            if self.items == []:
                return print('None')
            return self.items[-1]

        def __str__(self) -> str:
            return f"{self.items}"

    stack = Stack()
    brackets = {']': '[', ')': '(', '}': '{'}

    for item in lst_inp:

        if stack.items == []:
            stack.push(item)
            # print(stack)
            continue

        if item in list(brackets.keys()) and brackets[item] == stack.peek():
            # print(f'brackets[item] {brackets[item]}')
            # print(f'stack.peek() {stack.peek()}')
            stack.pop()
            # print(stack)
            continue

        stack.push(item)
    return stack.items == []


print(is_correct_bracket_seq(lst_inp))
