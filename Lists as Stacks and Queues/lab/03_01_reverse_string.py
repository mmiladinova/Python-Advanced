input_str = input()

reversed_str = ''
str_stack = []

for ch in input_str:
    str_stack.append(ch)

while str_stack:
    value = str_stack.pop()
    reversed_str += value

print(reversed_str)

