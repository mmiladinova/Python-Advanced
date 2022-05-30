parentheses_input = input()
parentheses_list = [str(x) for x in parentheses_input]
parentheses_stack = []

is_balanced = True
for index in range(len(parentheses_list)):
    if parentheses_list[index] == '(':
        parentheses_stack.append([parentheses_list[index], index])
    elif parentheses_list[index] == "{":
        parentheses_stack.append([parentheses_list[index], index])
    elif parentheses_list[index] == "[":
        parentheses_stack.append([parentheses_list[index], index])
    elif parentheses_list[index] == ')':
        opening_parenthesis = parentheses_stack.pop()[0]
        if opening_parenthesis != '(':
            is_balanced = False
            break
    elif parentheses_list[index] == '}':
        opening_parenthesis = parentheses_stack.pop()[0]
        if opening_parenthesis != '{':
            is_balanced = False
            break
    elif parentheses_list[index] == ']':
        opening_parenthesis = parentheses_stack.pop()[0]
        if opening_parenthesis != '[':
            is_balanced = False
            break

if is_balanced:
    print("YES")
else:
    print("NO")
