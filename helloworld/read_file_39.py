file_instance = open("sample.txt", 'r')

while True:
    line = file_instance.readline()
    if line == '':
        break

    print(line)

file_instance.close()
