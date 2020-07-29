#!/usr/bin/python3

import os


def get_list_of_files_in_directory(directory):
    a = []
    for item in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, item)):
            a.extend(get_list_of_files_in_directory(os.path.join(directory, item)))
        elif os.path.isfile(os.path.join(directory, item)):
            a.append(os.path.join(directory, item))
    return a


if __name__ == "__main__":
    currentdirectory = os.getcwd()
    total_num_lines = 0
    filesonly_list = get_list_of_files_in_directory(currentdirectory)

    for filename in filesonly_list:
        try:
            total_num_lines += sum(1 for line in open(filename, "r"))
        except:
            continue

    print(total_num_lines)
