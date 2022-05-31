input_str = input()
input_list = [float(x) for x in input_str.split()]

occurances_dict = {}

for num in input_list:
    if num not in occurances_dict:
        occurances_dict[num] = 0

    occurances_dict[num] += 1

for key, value in occurances_dict.items():
    print(f"{key} - {value} times")
