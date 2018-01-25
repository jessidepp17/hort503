# variable with tab in front of string; \t = tab character
tabby_cat = "\tI'm tabbed in."
# variable witha new line character in between the string
persian_cat = "I'm split\non a line."
# variable this backslaches within the string
backslash_cat = "I'm \\ a \\ cat." # question: why \\? if I wanted \ in the
                                   #    sting, I could've just used \
# new variable string object with many lines including tab and new line characters
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#printing all of the variables out
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
