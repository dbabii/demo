#!/usr/bin/env python3
import os
 
folder_path = "/home/grom/git/demo/dir_txt"
file_list = os.listdir(folder_path)

for i in file_list:
    print(i)

for i, file in enumerate(file_list, start=1):
    old_path = os.path.join(folder_path, file)
    name = f"file_{i}.txt"
    new_path = os.path.join(folder_path, name)
    os.rename(old_path, new_path)
