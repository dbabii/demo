#!/usr/bin/env python3

import os

files = {
        ".txt": "Text",
        ".pdf": "PDF",
        ".jpg": "Images",
        ".py": "Code"}


dir_path = "/home/grom/git/demo/dir"

files_list = os.listdir(dir_path)

for file in files_list:
    ext = os.path.splitext(file)[1]
    if ext in files:
        old_path = os.path.join(dir_path, file)
        dir_name = files[ext]
        dir_new_path = os.path.join(dir_path, dir_name)
        new_path = os.path.join(dir_new_path, file)
        os.makedirs(dir_new_path, exist_ok=True)
        print(f"Moving {file} -> {dir_name}/")
        os.rename(old_path, new_path)
    else:
        old_path = os.path.join(dir_path, file)
        dir_name = "Misc"
        dir_new_path = os.path.join(dir_path, dir_name)
        new_path = os.path.join(dir_new_path, file)
        os.makedirs(dir_new_path, exist_ok=True)
        print(f"Moving {file} -> {dir_name}/")
        os.rename(old_path, new_path)
