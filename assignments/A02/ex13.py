# imorting sys module; calling argument variable
from sys import argv
# defining four argument variables then add = argv
script, first, second, third = argv

# printing strings followed by the argument variable
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# you must remember to enter:
#    > python ex13.py one two three
#    you must enter the three argument variables when running the script
