COMMAND_LIST = {"list", "add", "edit", "delete", "average", "exit"}


def get_user_command() -> str:
    while True:
        command = input("Please input command: ")
        cmd = command.lower()
        if cmd not in COMMAND_LIST:
            print(f"{cmd} is not a valid command")
        else:
            return cmd
