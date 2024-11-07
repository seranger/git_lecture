# Question 1: Basic Function Definition and Calling

# TODO: Define a function called 'greet' that prints "Hello, World!"
def greet():
    return print(f"Hello, World!")
    
# TODO: Call the 'greet' function
greet()

#------------------------------------------------------------------------------------
# Question 2: Function with Parameters

# TODO: Define a function called 'personalized_greeting' that takes a name as a parameter and prints a personalized greeting
def personalised_greeting():
    name = input("name:")
    greeting= (f"Good Day, {name} I hope you are having a good day")
    return print(greeting)
# TODO: Call the 'personalized_greeting' function with your name
personalised_greeting()


#------------------------------------------------------------------------------------
# Question 3: Function with Return Value

# TODO: Define a function called 'square' that takes a number as a parameter and returns its square
def square(number):
    number_squared= number * number
    return print(f"your squared number is {number_squared}")

# TODO: Call the 'square' function with the number 5 and print the result
square(5)

#------------------------------------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value

# TODO: Define a function called 'rectangle_area' that takes length and width as parameters and returns the area of the rectangle
def rectangle_area():
    length= int(input("length of rectangle:"))
    width= int(input("width of rectangle:"))
    area_rectangle= length * width
    return print(f"the are of your rectangle is {area_rectangle}m^2")
# TODO: Call the 'rectangle_area' function with length 4 and width 5, and print the result
rectangle_area()

#------------------------------------------------------------------------------------
# Question 5: Using a Function as an Argument

# TODO: Define a function called 'apply_operation' that takes a function and a number as parameters, and returns the result of applying the function to the number
def apply_operation(function, x):
    return function(x)

# TODO: Define a function called 'double' that takes a number as a parameter and returns its double
def double(x):
    return x * 2 +7
# TODO: Use the 'apply_operation' function with the 'double' function and the number 7, and print the result
number= int(input("put in a number:"))

print(f"{apply_operation(double, number )}")


# TODO: Use the 'apply_operation' function with the 'square' function (defined in Question 3) and the number 3, and print the result

print(f"{apply_operation(square, 3)}")
