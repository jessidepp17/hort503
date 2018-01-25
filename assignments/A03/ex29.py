# variable list
people = 20
cats = 30
dogs = 15

# will only print if equation is true
if people < cats:
print("Too many cats! The world is doomed!")

if people > cats:
print("Not many cats! The world is saved!")

if people < dogs:
print("The world is drooled on!")

if people > dogs:
print("The world is dry!")

# same as coding 'dogs = dogs + 5' but short; this line is changing
#    dogs = 15 -> dogs = dogs + 5 from now on (dogs = 20)
dogs += 5

# will only print if equation is true
if people >= dogs:
print("People are greater than or equal to dogs.")

if people <= dogs:
print("People are less than or equal to dogs.")

if people == dogs:
print("People are dogs.")
