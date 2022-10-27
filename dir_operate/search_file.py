import os
import sys


def search_file(root_dir: str) -> list:
    result = []
    for dir, dir_names, file_names in os.walk(root_dir):
        for file in file_names:
            if file.lower().endswith(".txt"):
                result.append(f"{dir}/{file}")

    return result


def main():
    if len(sys.argv) <= 1:
        print("Please pass dir as an argument")
    else:
        file_list = search_file(sys.argv[1])
        print(file_list)


if __name__ == "__main__":
    main()
