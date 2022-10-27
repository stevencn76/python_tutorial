import os


def cwd():
    print(os.getcwd())
    os.chdir("mysub")
    print(os.getcwd())

    # os.mkdir("mysub2")

    # os.rename("mysub2", "mysub3")

    os.rmdir("mysub3")


def print_dir(root_dir: str):
    for root, dir_names, file_names in os.walk(root_dir):
        for dir in dir_names:
            print(f"{root}/{dir}")

        for file in file_names:
            print(f"{root}/{file}")


def main():
    print_dir("../../python_tutorial")


if __name__ == "__main__":
    main()
