# variable list
i = 0
numbers = []

while i < 6:
   print(f"At the top i is {i}")
   numbers.append(i)

   i = i + 1        # adding 1 to each i in order upto < 6
   print("Numbers now: ", numbers)
   print(f"At the bottom i is {i}")


print("The numbers: ")

# printing all of the numbers from the beginning (i=0) to end (i=5)
for num in numbers:
   print(num)
