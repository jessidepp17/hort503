# use ex16_test.txt as filename

# import module sys
from sys import argv

# one arg variable
script, filename = argv

# print formatted string with embedded variable; the code will erase the file
#    no matter what the user decides
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# prompt; printing ? first
input("?")

# printing string
print("Opening the file...")
# define new variable to open a file and ?
#  question: what does the 'w' do?
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# taking the target variable and calling the .truncate() function which seems
#    to erases file content
target.truncate()

print("Now I'm going to ask you for three lines.")

# defining new variables with input objects
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# taking the file and using the .write() function to rewrite txt into the file
#    first rewrites variable line1 object
target.write(line1)
# writes new line character into file
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# closes the file after rewriting by using .close() function
target.close()
