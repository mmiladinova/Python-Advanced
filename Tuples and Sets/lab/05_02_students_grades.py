number_of_students = int(input())

students_dict = {}

for student in range(number_of_students):
    name, st_grade = input().split(" ")
    grade = float(st_grade)

    if name not in students_dict:
        students_dict[name] = list()

    students_dict[name].append(grade)

for name, grades in students_dict.items():
    average_grade = sum(grades)/len(grades)
    formatted_grades = ' '.join(f'{grade:.2f}' for grade in grades)

    print(f"{name} -> {formatted_grades} (avg: {average_grade:.2f})")
