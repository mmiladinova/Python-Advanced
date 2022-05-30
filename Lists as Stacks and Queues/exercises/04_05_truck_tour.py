from collections import deque

number_of_pumps = int(input())

pumps = deque()

for _ in range(number_of_pumps):
    pumps.append([int(x) for x in input().split(" ")])


for count in range(number_of_pumps):
    trunk = 0
    is_failed = False
    for petrol, distance in pumps:
        trunk = trunk + petrol - distance
        if trunk < 0:
            is_failed = True
            break

    if is_failed:
        pumps.append(pumps.popleft())
    else:
        print(count)
        break
