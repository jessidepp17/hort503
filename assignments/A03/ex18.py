# This allows you to use arg variables without having to define them when
#    running the script (ex: > python ex18.py arg1 arg2). Now you just run
#    the script like normal and defing the args in the script

# defining two arg variables by using (*args) (used for fxns) instead of
#    'from sys import argv' by using the def (define fxn); must end line with :
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")   # printing formatted string with
                                           #    embedded variables

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

# define the arg variables in a list format much easier to change arguments in
#     a large script. only change arguments below and not throughout the script
#     and making a mistake
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
