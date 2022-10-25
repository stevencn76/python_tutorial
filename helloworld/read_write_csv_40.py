import csv


def read_csv(filename):
    file_instance = open(filename, encoding="UTF8")

    csv_reader = csv.reader(file_instance)

    for line in csv_reader:
        print(line)

    file_instance.close()


def write_csv(filename):
    file_instance = open(filename, "w", encoding="UTF8")

    csv_writer = csv.writer(file_instance)

    header = ['Name', 'Chinese', 'English', 'Math']
    rows = [
        ['Zhangsan', '80', '87', '100'],
        ['Lisi', '78', '79', '98'],
        ['Wangwu', '67', '90', '88']
    ]

    csv_writer.writerow(header)
    csv_writer.writerows(rows)

    file_instance.close()


def dict_write_csv(filename):
    file_instance = open(filename, "w", encoding="UTF8")

    header = ['name', 'chinese', 'english', 'math']

    csv_writer = csv.DictWriter(file_instance, header)
    rows = [
        {"name": 'Zhangsan',
         "chinese": '80',
         "english": '87',
         "math": '100'},
        {"name": 'Lisi',
         "chinese": '76',
         "english": '80',
         "math": '98'},
        {"name": 'Wangwu',
         "chinese": '60',
         "english": '77',
         "math": '90'}
    ]

    csv_writer.writeheader()
    csv_writer.writerows(rows)

    file_instance.close()


if __name__ == '__main__':
    filename = "students3.csv"

    # write_csv(filename)
    dict_write_csv(filename)
    read_csv(filename)
