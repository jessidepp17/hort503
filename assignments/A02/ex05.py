# defining variables
# variable wording must be in single quotes
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
# convert in to cm
height_cm = height * 2.54
# convert lbs to kg
weight_kg = weight * 0.453592

# printing "strings with {variables} embedded in them"; must use f to tell python
#    to format the string since there are variables in it
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {height_cm} centimeters tall.") # added height in cm
print(f"He's {weight} pounds heavy.")
print(f"He's {weight_kg} kilograms heavy.") # added weight in kg
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
# defining total variable
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
