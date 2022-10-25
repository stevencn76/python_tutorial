def process_list(student_data: dict):
    records = list(student_data.values())
    records.sort(key=lambda a: a.get("name"))

    for record in records:
        print(record.get("name"))
        print(f"Chinese score: {record.get('chinese')}")
        print(f"English score: {record.get('chinese')}")
        print(f"Math score: {record.get('chinese')}")
        print(" ")


def process_add(student_data: dict):
    pass


def process_edit(student_data: dict):
    pass


def process_delete(student_data: dict):
    pass


def process_average(student_data: dict):
    pass


def process_exit(student_data: dict):
    pass


def process_command(cmd: str, student_data: dict):
    if cmd == "list":
        process_list(student_data)
    elif cmd == "add":
        process_add(student_data)
    elif cmd == "edit":
        process_edit(student_data)
    elif cmd == "delete":
        process_delete(student_data)
    elif cmd == "average":
        process_average(student_data)
