# https://w.amazon.com/bin/view/Users/Jeneeb/Coding_Logical_and_Maintainable

import os
from stat import *

class FilePointer:
    def __init__(self, attrs):
        self.attrs = attrs


class FileNavigator:

    def scan(self, root_path):
        file_pointers = []

        with os.scandir(root_path) as entries:
            for entry in entries:
                stats = os.stat(entry)

                if not S_ISDIR(stats.st_mode):
                    file_pointer = FilePointer({"path": entry.path})
                    file_pointers.append(file_pointer)
                else:
                    sub_pointers = self.scan(entry.path)
                    file_pointers.extend(sub_pointers)

        return file_pointers


file_navigator = FileNavigator()
file_pointers = file_navigator.scan("/Users/rigupta/Desktop/")

for fp in file_pointers:
    print(fp.attrs["path"])