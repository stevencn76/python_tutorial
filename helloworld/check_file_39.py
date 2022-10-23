import os
import os.path as ospath
from pathlib import Path

print(ospath.exists("newfile2.txt"))
print(ospath.isfile("newfile.txt"))
print(ospath.isdir("newfile.txt"))

print("===============")
path = Path("sample.txt")
print(path.exists())
print(path.is_file())
print(path.is_dir())

# os.rename("newfile.txt", "newfile2.txt")
os.remove("newfile2.txt")
