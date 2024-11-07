# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name=input("name:")
# TODO: Ask the user for their age and store it in a variable
age=int(input("age:"))
# TODO: Print a greeting using the name and age variables
if age<18:
    print("Hey",name,"you are too young for this ride big boy")
elif age>=18:
    print("Hey Big Boy", name,"strap in and get ready for a bumpy ride ;)")
#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length=int(input("length in meters:"))
# TODO: Ask the user for the width of a rectangle and store it as an integer
width=int(input("width in meters:"))
# TODO: Calculate the area of the rectangle
area=length*width
# TODO: Print the result
print(area, "meters squared")
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
temperature=float(input("temperature:"))
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
fahrenheit=(temperature * (9/5)) + 32
# TODO: Print the result rounded to two decimal places
print(f"{fahrenheit:.2f} Degrees Fahrenheit")