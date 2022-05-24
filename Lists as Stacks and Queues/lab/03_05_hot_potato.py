from collections import deque

kids_input = input()
toss = int(input())

kids = deque(kids_input.split(" "))

counter = 0
while len(kids) > 1:
    counter += 1

    kid = kids.popleft()
    if counter == toss:
        print(f"Removed {kid}")
        counter = 0
    else:
        kids.append(kid)

print(f'Last is {"".join(kids)}')
