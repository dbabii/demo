#!/usr/bin/env python3
import os

path_to_dir = input("Please provide a full path to dir:\n")
keyword_case_sens = input("Please type a keyword (case-Sensitive):\n")

def recursive_search(path_to_dir):
    for root, dirs, files in os.walk(path_to_dir):
        for file in files:
            if file.endswith(".txt"):
                full_path = os.path.join(root, file)
                with open(full_path, "r") as f:
                    found = False
                    for line in f:
                        if keyword_case_sens in line:
                            if not found:
                                print(full_path)
                                found = True
                            print(line.strip())
                            

recursive_search(path_to_dir)
