# define variables
types_of_people = 10
# x is a variable that ouputs a string with embedded variable
x = f"There are {types_of_people} types of people."

# more variables and their values
binary = "binary"
do_not = "don't"
# y is another sting with embedded variables
y = f"Those who know {binary} and those who {do_not}."

# simple print value from x and y which result in strings since they
#    are variables
print(x)
print(y)

# printing strings with x and y variables
print(f"I said: {x}")
print(f"I also said: '{y}'")

# new variables
hilarious = False
# this variable is leaving space open so that I can code any given
#    variable later
joke_evaluation = "Isn't that joke so funny?! {}"

# print a string using .format(); you call the joke_evaluation variable
#    and then you .format another variable into the joke_evaluation string
print(joke_evaluation.format(hilarious))

# new variables
w = "This is the left side of..."
e = "a string with a right side."

# printing the addition of two variable values; w is the first half of a
#    string and e is the other half
print(w + e)
