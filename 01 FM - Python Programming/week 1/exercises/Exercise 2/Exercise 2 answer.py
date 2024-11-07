# Question 1: Arithmetic and Assignment Operators
'''
# TODO: Add 3 to x using the += operator
x=0
x += 3
# TODO: Multiply y by 2 using the *= operator
y=1
y *= 2
# TODO: Divide x by y and store the result in a variable called 'result'
result = x/y
# TODO: Print the value of 'result'
print(result)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a= int(input("a="))
b= int(input("b="))
c= int(input("c="))

if a>b:
    print(a , "is greater than" , b)
else:
    print(a , "is less than" , b)
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
if b%2==0:
    print(b, "is even")
# TODO: Create a condition that checks if c is less than or equal to a
if c>=a:
    print(c , "is greater than or equal to" , a)
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_condition= False
if a>b or b%2==0 and c<=a:
    final_condition=True
# TODO: Print the value of 'final_condition'
print(final_condition)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score= int(input("test score between 0-100:"))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F

if score>=90:
    grade="A"
if score>=80 and score<90:
    grade="B"
if score>=70 and score<80:
    grade="C"
if score>=60 and score<70:
    grade="D"
if score<=59:
    grade="F"

# TODO: Print the grade for the given score
print(grade)'''
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1= int(input("first score "))
num2= int(input("second score "))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation= input("+,-,*,/ ")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2

if operation == '-':
    a = num1-num2
if operation== '+':
    a= num1+num2
if operation== '*':
    a= num1*num2

if operation== '/':
    if num2!=0:
        a= num1/num2
    else: 
        print("undefined")

print(f'{a}')
# TODO: Handle the case of division by zero


# TODO: Print the result of the operation
