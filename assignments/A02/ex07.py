# printing string
print("Mary had a little lamb.")
# printing a string with embedded variable, but the variable was not
#    previously defined. So you can add a variable value by calling
#    the .format() function; remember to add quotes to the variable
#    value since it is not a defined variable name
print("Its fleece was white as {}.".format('snow'))
# printing new string
print("And everywhere that Mary went.")
# printing sting "." 10 times in a new line
print("." * 10)

# defining variables which have values that are strings
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# printing varialbes end1-end6 all in a row without spaces but then
#    you add a space at the end of the equation and print the following
#    print() at the end of the previous one. If I remove the  end = ""
#    the following string will print on a new line not together anymore
print(end1 + end2 + end3 + end4 + end5 + end6, end = " ")
print(end7 + end8 + end9 + end10 + end11 + end12)
