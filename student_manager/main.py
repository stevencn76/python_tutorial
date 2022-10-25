from command.user_command import get_user_command
from command.command_processor import process_command
from store.csv_store import load_data, save_data


def main():
    try:
        student_data = load_data()
    except:
        print("Error happened")
        return

    while True:
        command = get_user_command()
        if command == "exit":
            break

        process_command(command, student_data)

    try:
        save_data(student_data)
    except:
        print("Error happened")


if __name__ == "__main__":
    main()