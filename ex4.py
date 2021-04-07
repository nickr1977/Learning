# Variable to define the number of cars
cars = 100

# Variable to define the seats avaibable in a car
space_in_car = 4

# Variable to define the amount of drivers available
drivers = 30

# Variable to define the number of passengers needing rides
passengers = 90

# Variable to define the amount of cars that do not have drivers
cars_not_driven = cars - drivers

# Variable to define the amount of cars with drivers, also equal to the drivers variable
cars_driven = drivers

# Variable to define the space in a car available for passengers
carpool_capacity = cars_driven * space_in_car

# Variable to define the number of average passengers per car, created by dividing passengers by cars driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers avaiable.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
