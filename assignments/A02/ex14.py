# importing sys; using argument variable
from sys import argv

# one argument variable defined
script, user_name = argv
# defining variable using > when prompting for answers
prompt = '> '

# formatting sting with embedded variables and printing
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
# defining new variable object will be the prompt answer with '>'
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# printing string with many lines and enbedded variable answers from prompts
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

# dont forget to run the script as follows:
#    python ex14.py Jessio (this is the user_name)
