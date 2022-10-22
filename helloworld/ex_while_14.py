tip = 'Please enter a grade(type "exit" to quit): '

summary = 0
count = 0
running = True
while running:
    s_grade = input(tip)
    if s_grade == 'exit':
        running = False
    else:
        grade = int(s_grade)

        if grade < 0 or grade > 100:
            print('Invalid grade')
        else:
            summary = summary + grade
            count = count + 1

            if grade < 59:
                print('Not pass')
            elif grade < 75:
                print('Pass')
            elif grade < 85:
                print('Good')
            else:
                print("Excellent")

average = summary / count
print(f'Average: {average}')
