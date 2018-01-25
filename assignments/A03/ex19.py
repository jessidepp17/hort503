# defining 2 arg variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
# define values for arg variables directly
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
# define variable objects by creating new variables
amount_of_cheese = 10
amount_of_crackers = 50

# I think this is creating new argv but why not use def fxn like line 2?
#    or is this just adding two new variable labels for cheese_and_crackers
#    so that you don't keep using the same argument names? why is this useful?
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# NOTE: the last two blocks are just objects that keep getting into the
#    the variables embedded in line 2 block, I think.
