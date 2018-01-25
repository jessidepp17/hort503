# from_file use ex15_sample.txt
# to_file use ex16_test.txt

from sys import argv
from os.path import exists

# defining 2 arg variables
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# defining variable object which opens the from_file
in_file = open(from_file)
# defining variable object which uses the .read() fxn to read the from_file
indata = in_file.read()

# string embedded with variable but also prints the byte length of the file
#    using len()
print(f"The input file is {len(indata)} bytes long")

# embedded variable checks to see if the to_file exists printing TRUE or FALSE
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
# prompt
input()

# new variables to open the to_file and write the from_file txt into the to_file
out_file = open(to_file, 'w')
out_file.write(indata)

# printing string
print("Alright, all done.")

# closes both files after the swap
out_file.close()
in_file.close()
