# Files in python

# Files are required to handle persistent data

# File modes:
# r - read, if does not exists throw error
# w - write and create
# a - append and create
# x - create, if exists throw error

# t - text
# b - binary

file_obj = open("example_file.txt", mode="rt")
for i in file_obj:
    print(i)

import os

os.remove("example_file.txt")


