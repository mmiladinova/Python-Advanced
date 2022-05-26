cloths_values_stack = list(input().split())
rack_capacity = int(input())

racks_quantity = 1
counter = 0

while cloths_values_stack:

    cloth_value = int(cloths_values_stack.pop())
    counter += cloth_value

    if rack_capacity == counter and cloths_values_stack:
        racks_quantity += 1
        counter = 0
    elif counter > rack_capacity:
        racks_quantity += 1
        counter = cloth_value

print(racks_quantity)
