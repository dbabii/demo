#!/usr/bin/env python3

import os

files = {
        ".txt": "Text",
        ".pdf": "PDF",
        ".jpg": "Images",
        ".py": "Code"}


dir_path = "/home/grom/git/demo/dir"
files_list = os.listdir(dir_path)

# move repetable blocks under one function
def move_file(file, dir_name):
    old_path = os.path.join(dir_path, file)
    new_dir = os.path.join(dir_path, dir_name)
    new_path = os.path.join(new_dir, file)
    os.makedirs(new_dir, exist_ok=True)
    print(f"Moving {file} -> {dir_name}/")
    os.rename(old_path, new_path)


for file in files_list:
    ext = os.path.splitext(file)[1]
    if ext in files:
        move_file(file, files[ext])
    else:
        move_file(file, "Misc")
