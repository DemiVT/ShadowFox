# 1. Write a function that takes two arguments and uses the format function
def format_function(value1, value2):
    return "Formatted output: {} {}".format(value1, value2)

print(format_function(145, 'o'))

# 2. Calculate the area of the pond and the total amount of water
import math

radius = 84
pi = 3.14
pond_area = pi * (radius ** 2)
water_per_sqm = 1.4
total_water = pond_area * water_per_sqm
print("Total amount of water in the pond:", int(total_water))

# 3. Calculate speed in meters per second
distance = 490  # meters
time = 7 * 60  # converting minutes to seconds
speed = distance / time
print("Speed in meters per second:", int(speed))
