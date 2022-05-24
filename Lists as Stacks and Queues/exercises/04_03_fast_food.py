from collections import deque

food_quantity = int(input())
orders = deque(input().split(" "))

max_num = 0
for num in orders:
    num = int(num)
    if num > max_num:
        max_num = num

print(max_num)

while True:
    if orders:
        order = int(orders[0])

    if food_quantity - order >= 0:
        food_quantity -= order
        if orders:
            orders.popleft()
    else:
        break

if orders:
    print(f"Orders left: {' '.join(orders)}")
else:
    print(f"Orders complete")
