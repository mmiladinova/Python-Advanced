from collections import deque

water_quantity = int(input())
queue = deque()

while True:
    command = input()
    if command == "Start":
        break

    queue.append(command)

while command != 'End':
    command = input()
    if command.isdigit():
        if water_quantity - int(command) >= 0:
            water_quantity -= int(command)
            print(f"{queue.popleft()} got water")
        else:
            person = queue.popleft()
            print(f"{person} must wait")
    elif 'refill' in command:
        water = command.split(" ")
        water_quantity += int(water[1])

print(f"{water_quantity} liters left")
