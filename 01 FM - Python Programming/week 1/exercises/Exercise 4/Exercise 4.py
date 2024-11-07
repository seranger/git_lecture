# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
list_of_fruits= ['apples', 'bannanas', 'grapes']
    
# TODO: Use a for loop to print each fruit in the list
for x in list_of_fruits:
    print(f"{x}")
    
print("---Question 1 Complete---")
#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count=5

while count !=0:
    print(count)
    count -=1
print("---Question 2 Complete---")
#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
sqaure_numbers= range(1, 11)

for x in sqaure_numbers:
    x= x**2
    print(x)
print("---Question 3 Complete---")
#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
# TODO: Use a for loop to select and print 3 random colors from the list
for _ in range(3):  
    random_color = random.choice(colors)  
    print(random_color)
print("---Question 4 Complete---")
#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:


# TODO: Import the custom module and use its functions
import math_operations

# TODO: Use a while loop to create a simple calculator
def calculator():
    print("Welcome to the simple calculator!")
    while True:
        
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':  
            print("Exiting calculator. Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            print(f"Result: {math_operations.add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {math_operations.subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {math_operations.multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {math_operations.divide(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid operation.")

calculator()
print("---Question 5 Complete---")