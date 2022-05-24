n = int(input())

stack = []

for line in range(n):
    command = input()

    if command.startswith("1 "):
        command_list = command.split(" ")
        number = int(command_list[1])
        stack.append(number)

    elif command == "2":
        if stack:
            stack.pop()

    elif command == "3":
        if stack:
            print(max(stack))

    elif command == "4":
        if stack:
            print(min(stack))

reversed_list = []
while stack:
    reversed_list.append(str(stack.pop()))

print(", ".join(reversed_list))
