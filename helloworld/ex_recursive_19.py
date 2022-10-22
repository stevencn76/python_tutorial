# sample 1: print sequence
def print_sequence(n: int):
    print(n)

    next_num = n - 1
    if next_num > 0:
        print_sequence(next_num)


print_sequence(10)


# sample 2: summary a sequence
def summary(n):
    if n == 1:
        return 1

    return n + summary(n - 1)


print(summary(100))


# sample 3: n!
def nn(n):
    if n == 1:
        return 1

    return n * nn(n - 1)


print(nn(4))

