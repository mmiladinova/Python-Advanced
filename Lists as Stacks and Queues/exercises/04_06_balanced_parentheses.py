parentheses_input = input()
parentheses_list = [str(x) for x in parentheses_input]
opening_brackets_stack = []

pairs = {
    "(": ")",
    "{": "}",
    "[": "]"
}

is_balanced = True
for ch in parentheses_list:
    if ch in "({[":
        opening_brackets_stack.append(ch)
    elif not opening_brackets_stack:
        is_balanced = False
    else:
        last_opening_bracket = opening_brackets_stack.pop()
        if pairs[last_opening_bracket] != ch:
            is_balanced = False

    if not is_balanced:
        break

if is_balanced and len(opening_brackets_stack) == 0:
    print("YES")
else:
    print("NO")
