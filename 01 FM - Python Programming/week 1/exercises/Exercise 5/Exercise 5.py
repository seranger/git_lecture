# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits= ["grapes","bannanas","watermelon","apples","peachs","mango",]

# TODO: Add a fruit to the end of the list
fruits.append("blueberry")
# TODO: Insert a fruit at the beginning of the list
fruits.insert(0,"blueberry")
# TODO: Remove a fruit from the list
fruits.remove("mango")
# TODO: Print the modified list
print(fruits)
print("---End Question 1---")
#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers= [1,2,3,4,5]
# TODO: Create a new list with each number squared
squared= [i**2 for i in numbers]
# TODO: Find the sum and average of the original numbers
sum= 0 

for i in numbers:
    sum+= i
avg= sum/len(numbers)
# TODO: Print the results
print(int(avg))
print("---End Question 2")
#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
country_and_capital={
    "South Africa": "Pretoria"
}
# TODO: Add a new country-capital pair
country_and_capital["England"]="London"
# TODO: Update the capital of an existing country
country_and_capital["England"]="Brazilia"
# TODO: Remove a country-capital pair
del country_and_capital["South Africa"]
# TODO: Print the modified dictionary
print(country_and_capital)
print("---End of Question 3---")
#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors={
    "mango": "yellow",
    "orange": "orange",
    "dragonfruit": "pink",
    "strawberry": "red"
}
# TODO: Print all the fruits (keys)
for fruit in fruit_colors.keys():
    print(fruit)
# TODO: Print all the colors (values)
for colors in fruit_colors.values():
    print(colors)
# TODO: Print each fruit and its color
print(fruit_colors)
# TODO: Check if a fruit is in the dictionary and print its color
fruit_checker= "strawberry"
if fruit_checker in fruit_colors:
    print(f"the color of your {fruit_checker} is {fruit_colors[fruit_checker]}")

print("---End of Question 4")