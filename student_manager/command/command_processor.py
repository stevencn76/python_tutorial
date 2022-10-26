from common import course_def


def process_list(student_data: dict):
    records = list(student_data.values())
    records.sort(key=lambda a: a.get("name"))

    for record in records:
        print(record.get("name"))
        for course in course_def.COURSE_NAME_SET:
            print(f"{course} score: {record.get(course)}")
        print(" ")


def process_add(student_data: dict):
    name = input("Please input name: ")
    chinese_score = input("Please input chinese score: ")
    english_score = input("Please input english score: ")
    math_score = input("Please input math score: ")

    record = {
        "name": name,
        "chinese": chinese_score,
        "english": english_score,
        "math": math_score
    }

    student_data[name] = record
    print(f"Added student scores for '{name}' successfully")


def process_edit(student_data: dict):
    name = input("Please input name: ")
    if name in student_data.keys():
        course = input("Please input course name: ")
        if course in course_def.COURSE_NAME_SET:
            score = input("Please input score: ")
            student_data[name][course] = score
            print(f"Update score for '{name}' successfully")
        else:
            print(f"Course '{course}' is not supported")
    else:
        print(f"Student '{name}' does not exist")


def process_delete(student_data: dict):
    name = input("Please input name: ")

    if name in student_data.keys():
        student_data.pop(name)
        print(f"Delete '{name}' successfully")
    else:
        print(f"Student '{name}' does not exist")


def process_average(student_data: dict):
    student_count = len(student_data)
    if student_count == 0:
        print("No student scores")
        return

    total_results = {}
    for course in course_def.COURSE_NAME_SET:
        total_results[course] = 0

    for record in student_data.values():
        for course in course_def.COURSE_NAME_SET:
            total_results[course] = total_results[course] + int(record.get(course))

    for course in course_def.COURSE_NAME_SET:
        average = total_results[course] / student_count
        print(f"Average of {course} is: {average}")


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
