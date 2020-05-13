# Take input of you and your neighbor
your_first_name = input("What is your name? ")
neighbor_first_name = input("What is your neighbor's name? ")

# Take input how long each of you have been gaming
years_you_gamed = input("How many years have you been gaming? ")
years_neighbor_gamed = input("How many years has your neighbor been gaming? ")

# Add total years
total_years_gamed = int(years_you_gamed) + int(years_neighbor_gamed)

# Print results
print("I am " + your_first_name + " and my neighbor is " + neighbor_first_name)
print("Together we have been gaming for " + str(total_years_gamed) + " years!")