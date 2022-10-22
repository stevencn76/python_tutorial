def get_user_input() -> list:
    result_list = []
    while True:
        s_grade = input("Enter a grade(type 'exit' to quit):")
        if s_grade == 'exit':
            break

        result_list.append(int(s_grade))

    return result_list


def get_average(grade_list: list) -> float:
    count = len(grade_list)

    if count == 0:
        return 0

    total = 0
    for g in grade_list:
        total = total + g

    return total / count


def get_grades_above_average(grade_list: list, average: float) -> list:
    res_list = []
    for g in grade_list:
        if g > average:
            res_list.append(g)

    return res_list


grade_list = get_user_input()
average = get_average(grade_list)
grades_above_average = get_grades_above_average(grade_list, average)

print(f'Average: {average}')
print(f'Grades above average: {grades_above_average}')