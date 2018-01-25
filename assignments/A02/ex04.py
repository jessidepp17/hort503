# defining variables
# there are 100 cars
cars = 100
# there is space for 4.0 people in a car
space_in_a_car = 4.0
# there are 30 drivers
drivers = 30
# there are 90 passengers
passengers = 90
# only 30 drivers for 100 cars so just subtract
cars_not_driven = cars - drivers
# driven cars = the number of drivers available
cars_driven = drivers
# cars driven multilied by capacity per car is carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# number of passengers per car = total passengers divided by cars driven
average_passengers_per_car = passengers / cars_driven

# printing sentences with strings and variables; variable names are printed as
#    the values disignated to the variable since it is not coded as a string
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
