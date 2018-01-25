# use ex20_test.txt as input_file

# import sys; using argv in this script
from sys import argv

# defining 1 argv
script, input_file = argv

# defining arg variable f which is the file
def print_all(f):
    print(f.read())   # read the file and print

# def function  argv called rewind
def rewind(f):
    f.seek(0)        # this will .seek() fxn, this will move the file to
                     #    the 0 byte (1st byte) in the file

# defining new argv; 2 of them
def print_a_line(line_count, f):
    print(line_count, f.readline())

# defining variable which will opent the input_file
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

#  Question: I dont really understand the order of this script
