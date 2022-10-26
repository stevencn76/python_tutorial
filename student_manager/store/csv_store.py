import csv
import os.path

file = "students.csv"


def load_data() -> dict:

    result = {}

    if os.path.exists(file):
        file_instance = open(file, encoding="UTF8")
        csv_reader = csv.DictReader(file_instance)

        for row in csv_reader:
            name = row.get("name")
            result[name] = row

    # result["zhangsan"] = {"name": "zhangsan", "chinese": 89, "english": 90, "math": 100}

    return result


def save_data(data: dict):
    file_instance = open(file, 'w', encoding="UTF8")

    if len(data) > 0:
        rows = list(data.values())
        csv_writer = csv.DictWriter(file_instance, rows[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(rows)

    file_instance.close()
