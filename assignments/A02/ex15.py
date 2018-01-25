# import from sys; argv used
from sys import argv

# defining one arg variable asking for a file name
script, filename = argv

# defing new variable called txt that will open filename
txt = open(filename)

# print string with embedded filename
print(f"Here's your file {filename}:")
# this will open the file and print out the file contents
print(txt.read())

# string that asks the user to input the filename after ">"
print("Type the filename again:")
file_again = input("> ")

# define new variable; prompts the filename and opens that file
txt_again = open(file_again)
# print txt variable with .read() funtction to print file content
print(txt_again.read())

# > python ex15.py ex15_sample.txt
