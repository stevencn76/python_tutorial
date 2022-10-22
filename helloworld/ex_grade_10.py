tip = 'Please input a grade: '
str_grade = input(tip)
grade = int(str_grade)

if grade < 0 or grade > 100:
    print("Invalid grade")
elif grade <= 59:
    print('Not pass')
elif grade <= 75:
    print('Pass')
elif grade <= 85:
    print('Good')
else:
    print("Excellent")
