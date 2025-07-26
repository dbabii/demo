#!/usr/bin/env python3
import os
 
folder_path = "/home/grom/git/demo/dir_txt"
file_list = os.listdir(folder_path)

def print_files():
    file_list = os.listdir(folder_path)
    for i in file_list:
        print(i)

print("Before changing:")
print_files()

for i, file in enumerate(file_list, start=1):
    old_path = os.path.join(folder_path, file)
    # save original extension
    ext = os.path.splitext(file)[1]
    name = f"file_{i}{ext}"
    new_path = os.path.join(folder_path, name)
    os.rename(old_path, new_path)

print("After changing:")
print_files()
