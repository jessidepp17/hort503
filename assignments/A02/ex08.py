# variable called formatter defined
formatter = "{} {} {} {}"

# using .format() function to input values into the formatter variable
#    since there are four {} in formatter variable, you can place four
#    different values into these place holders. Must separate the objects
#    with commas
print(formatter.format(1, 2, 3, 4))
# formatting stings into the {} of the defined variable formatter
print(formatter.format("one", "two", "three", "four"))
# formatting more objects into the formatter varialbe
print(formatter.format(True, False, False, True))
# formatting the variable into itself one string for each {}
print(formatter.format(formatter, formatter, formatter, formatter))
# formatting strings into each {} but coding on new lines BUT dont
#    dont forget the commas to designate {} position
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))
