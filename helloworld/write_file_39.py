file_instance = open("sample.txt", 'w')  # 'w' - overwrite

file_instance.write("This is new string\n")

file_instance.writelines(["aaaaa\n", "bbbbbb\n", "cccccc\n"])

file_instance.close()
