expression = input()

brackets_stack = []

for index in range(len(expression)):
    ch = expression[index]
    if ch == '(':
        brackets_stack.append(index)
    elif ch == ')':
        start = brackets_stack.pop()
        end = index + 1
        print(expression[start:end])
