tip = 'Enter number '
s_num1 = input(tip + '1: ')
s_num2 = input(tip + '2: ')

start = int(s_num1)
stop = int(s_num2) + 1

result = 0
for num in range(start, stop):
    result = num + result

print(f'Summary: {result}')


# 1: num + result -> result
# 2: num + result -> result
# 3: num + result -> result
