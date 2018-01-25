# printing a string followed by a space and telling python to avoid a \n
print("How old are you?", end=' ')
# defining new variable but using input() function so that someone can input
#    something when running the script. it is prompting the user to respond
age = input()
# printing sting + space + input in one line
print("How tall are you?", end=' ')
# variable requesting input from user
height = input()
# printing sting + space + input in one line
print("How much do you weigh?", end=' ')
# variable requesting input from user
weight = input()

# formatting a string with embedded variables; this will place each input response
#    into the string. cool!
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# study drill
print("What is your full name?", end= " ")
users_name = input()
print("What is your favorite color?", end= " ")
color = input()
print(f"Yur name is {users_name} and your favorite color is {color}, right?")
