"""1)print('hello')
print("wel come")
print(''' welcome to python''')
print("hi this is demo")"""

"""2)print("manual")
a = 10
print(type(a))
a = "hello"
print(type(a))
a = 10.0
print(type(a))
a = True
print(type(a))

print('using type method')
a = input("enter data a")
print(type(a))
a = int(input("enter data a"))
print(type(a))
a = float(input("enter data a"))
print(type(a))"""

"""3)a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)"""

"""4)x = 10
y = 20
print("Equal to:", x == y)
print("Not equal to:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal to:", x >= y)
print("Less than or equal to:", x <= y)"""

"""5)p = True
q = False

print("AND:", p and q)

print("OR:", p or q)

print("NOT:", not p)"""

#6. wp to Swap the 2 numbers without tem
"""a = int(input("enter a number a  "))
b = int(input("enter a number b  "))

print("direct swap")
a, b = b, a
print(a)
print(b)"""

#7. wp to Swap the 2 numbers with tem
"""a = int(input("enter a number a  "))
b = int(input("enter a number b  "))

print("temp way")
tem = a
a = b
b = tem
print(a)
print(b)"""

#8. wp to Swap the 2 numbers using addition an subtraction
"""a = int(input("enter a number a  "))
b = int(input("enter a number b  "))

print("add method")
a = a + b
b = a - b
a = a - b
print(a)
print(b)"""

#9. wp to Swap the 2 numbers using multiplication an division
"""a = int(input("enter a number a  "))
b = int(input("enter a number b  "))

print("mul ")
a = a*b
b = a/b
a = a/b
print(a)
print(b)"""

#10. Write a program to calculate salesman purchase 50caps at the rate of 500rs what the cost of 1 cap. will be.
"""caps_purchased = 50
total_cost = 500
cost_per_cap = total_cost / caps_purchased
print("The cost of 1 cap will be:", cost_per_cap, "Rs")"""

#11. Write a program to calculate salesman buys 100 bags at the cost of 1000rs out of 100 bags 12 bags are damaged what is the cost of 1 bag
"""bags_purchased = 100
total_cost = 1000
damaged_bags = 12
bags_remaining = bags_purchased - damaged_bags
cost_per_bag = total_cost / bags_remaining
print("The cost of 1 bag will be:", cost_per_bag, "Rs")"""

#12. Write a program to calculate a salesman purchase 100 caps at the cost of 1000rs 10 caps are damaged and 200rs is used for food 300es for traveling what is the cost of 1 cap.
"""caps_purchased = 100
total_cost = 1000
damaged_caps = 10
additional_expenses = 200 + 300  # Food cost + Travel cost
net_cost = total_cost - additional_expenses
caps_remaining = caps_purchased - damaged_caps
cost_per_cap = net_cost / caps_remaining
print("The cost of 1 cap will be:", cost_per_cap, "Rs")"""

#13 negetive or positive number
"""number_to_check = -12

if number_to_check > 0:
    result = "Positive"
elif number_to_check < 0:
    result = "Negative"
else:
    result = "Zero"

print(f"The number {number_to_check} is {result}.")"""

#14write a program to check the give number is even or odd in
"""number_to_check = 17

if number_to_check % 2 == 0:
    result = "Even"
else:
    result = "Odd"

print(f"The number {number_to_check} is {result}.")"""

#15.write a program to find the greatest of 2 number
"""num1 = 25
num2 = 37

if num1 > num2:
    greatest_num = num1
else:
    greatest_num = num2

print(f"The greatest number between {num1} and {num2} is {greatest_num}.")"""

#16Write python code to check leap year.
"""year_to_check = 2024

if (year_to_check % 4 == 0 and year_to_check % 100 != 0) or (year_to_check % 400 == 0):
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")"""

#17.Write java code to display the following messages
#if a number divides by 3 display hello
#if number divides by 5 display hi
#if number divides by 3 and 5 display hello hi 3,10,15
"""number = 15

if number % 3 == 0 and number % 5 == 0:
    print("hello hi")
elif number % 3 == 0:
    print("hello")
elif number % 5 == 0:
    print("hi")"""

#18Write java code to read 3 sides of triangle and display what type of triangle it is
"""side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")"""

#19.write a program to check is the user is eligible for driving licenses whose age is 17 years
"""age = 16

if age >= 18:
    print("You are eligible for a driving license.")
else:
    print("You are not eligible for a driving license.")"""

#21.write a program to find greatest of 3 numbers
"""num1 = 25
num2 = 37
num3 = 20

if num1 >= num2 and num1 >= num3:
    print(f"The greatest number is {num1}.")
elif num2 >= num1 and num2 >= num3:
    print(f"The greatest number is {num2}.")
else:"""

#22Write a program to check if a character is a vowel or consonant.
"""char = 'a'

if char.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")"""

#23 write a program to display the result with respect to the marks
#if the marks is 35 to 50 display pass
#if the marks is 50 to 60 display 2nd class
#if the marks is 60to75 first class
#75to 100 distinction else fail.
"""marks = 65

if marks >= 35 and marks < 50:
    print("Pass")
elif marks >= 50 and marks < 60:
    print("2nd class")
elif marks >= 60 and marks <= 75:
    print("First class")
elif marks > 75 and marks <= 100:
    print("Distinction")
else:
    print("Fail")
for num in range(20, 9, -1):
    print(num)"""

#24Create a program to calculate the sum of natural numbers using a while loop
"""num = 10
sum = 0
while num > 0:
    sum = sum + num
    num -= 1
print("Sum of natural numbers from 1 to 10:", sum)"""


#25.write a program to display all even number from 1 to 20
"""for num in range(2, 21, 2):
    print(num)
#26.write a program to display numbers from 1 to 30 which are divisible by 3
for num in range(1, 31):
    if num % 3 == 0:
        print(num)"""


#27.write a program to display the following messages for the range 1 to 30
#if the number divided by 3 display hi
#if no divides by 5 display hello
#if a number divides by 3 and 5 display hi hello
"""for num in range(1, 31):
    if num % 3 == 0 and num % 5 == 0:
        print("hi hello")
    elif num % 3 == 0:
        print("hi")
    elif num % 5 == 0:
        print("hello")"""


#28.write a java code to read a number and check is it a palindrome
"""number = input("Enter a number: ")
is_palindrome = True

for i in range(len(number) // 2):
    if number[i] != number[-i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")"""


#29.Display Prime Numbers from 1 to 50:
"""for num in range(1, 51):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)"""


#30.write a program to display fibanocci series upto 15 using loops
"""a, b = 0, 1
print(a)
for _ in range(14):
    print(b)
    a, b = b, a + b"""


#31.Display Factorial of a Number using Loops:
"""number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial =factorial * i

print(f"Factorial of {number} is {factorial}.")"""


#32.Implement a program to print the pattern:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
"""rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()"""


#33Write a program to generate a pattern:
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5
"""rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print(0)"""


#37.Write a program to generate a pattern:

"""rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("", end=" ")
    print()"""

#38
"""for i in range(1,10):
    if(i==6):
        break;
    print(i)"""

#39
"""for i in range(1, 10):
    if (i == 3):
        continue;
    print(i)"""

#40my_string = "Python"

"""print(my_string[0])  # Output: 'P'
print(my_string[1])
print(my_string[2])
print(my_string[3])
print(my_string[-1])  # Output: 'n'
print(my_string[2:5])  # Output: 'tho'"""

#41
"""single_quoted_string = 'Hello, World!'
double_quoted_string = "Hello, Python!"
multi_line_string = '''This is a multi-line string.'''"""

#42
"""str1 = "Hello"
str2 = "World"

concat_string = str1 + ", " + str2
print(concat_string)"""


#43
"""name = "Alice"
age = 30

formatted_string = f"Name: {name}, Age: {age}"
print(formatted_string)  # Output: 'Name: Alice, Age: 30'"""

#44
"""my_string = "   Hello, World!   "

print(my_string.upper())  # Output: '   HELLO, WORLD!   '
print(my_string.strip())  # Output: 'Hello, World!'

words = my_string.split(",")
print(words)  # Output: ['   Hello', ' World!   ']"""


 #45.# Create a list
"""my_list = [1, 2, 3, 'apple', 'banana', True]

print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: True

my_list[3] = 'cherry'
print(my_list)  # Output: [1, 2, 3, 'cherry', 'banana', True]

my_list.append('orange')
print(my_list)  # Output: [1, 2, 3, 'cherry', 'banana', True, 'orange']

my_list.remove('banana')
print(my_list)  # Output: [1, 2, 3, 'cherry', True, 'orange']
Tuples:
Tuples are ordered, immutable (unchangeable), and can contain elements of different d6.6ata types."""


46.
# Create a tuple
"""my_tuple = (1, 2, 3, 'apple', 'banana')

print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 'banana'

new_tuple = my_tuple + ('cherry', 'orange')
print(new_tuple)  # Output: (1, 2, 3, 'apple', 'banana', 'cherry', 'orange')
Sets:
Sets are unordered, mutable (modifiable), and contain unique elements 7(no duplicates)."""


47.
# Create a set
"""my_set = {1, 2, 3, 'apple', 'banana', 'apple'}

my_set.add('cherry')
print(my_set)  
my_set.remove('banana')
print(my_set)  

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2)) 
print(set1.intersection(set2))  
Dictionaries:
Dictionaries are unordered, mutable (modifiable), and store data in key-value pairs (keys must be unique)."""


#48.
"""[
Built-in Math Functions:
Python provides several built-in math functions that can be used without importing any module. Here are some of the commonly used ones:
1.abs(x): Returns the absolute value of a number x."""


#49.
"""num = -5
abs_num = abs(num)
print(abs_num)"""

#2.max(iterable): Returns the maximum value from an iterable
#50.
"""numbers = [3, 7, 2, 9, 5]
max_num = max(numbers)
print(max_num)  # Output: 9
3.min(iterable): Returns the minimum value from an iterable."""


#51.
"""numbers = [3, 7, 2, 9, 5]
min_num = min(numbers)
print(min_num)  # Output: 2
4.pow(x, y): Returns x raised to the power of y."""

#52.
"""result = pow(2, 3)
print(result)  # Output: 8
5.round(x, n): Rounds the number x to n decimal places."""

#53.
"""num = 3.14159
rounded_num = round(num, 2)
print(rounded_num) 
The Math Module:
The math module in Python provides more advanced mathematical functions and constants. To use functions from 
the math module, you need to import it first:
import math
1.math.sqrt(x): Returns the square root of x."""

#54.
"""import math

result = math.sqrt(25)
print(result)  # Output: 5.0
2.math.factorial(x): Returns the factorial of x."""

#55.
"""import math

result = math.factorial(5)
print(result)"""


#3.math.sin(x), math.cos(x), math.tan(x): Returns the sine, cosine, and tangent of an angle in radians.
#56.
"""import math

angle = math.pi / 4
sin_val = math.sin(angle)
cos_val = math.cos(angle)
tan_val = math.tan(angle)

print(sin_val, cos_val, tan_val) 
4.math.log(x, base): Returns the logarithm of x with the specified base."""

#57.
"""import math

result = math.log(100, 10)
print(result)"""


#5.math.pi, math.e: Constants representing π and Euler's number (e).
#58.
"""import math

print(math.pi) 
print(math.e)"""

#59
"""def greet(name):
    print(f"Hello, {name}!")
greet("Alice")"""

#60
"""import mymodule as mm
mm.greet("Bob")"""


#61.Display "Hello, World!" using a method:
"""def say_hello():
    print("Hello, World!")

say_hello()"""


#62.Calculate the square of a number using a method:
"""def square(num):
    return num ** 2

result = square(5)
print("Square:", result)"""


#63.Calculate the sum of two numbers using a method:
"""def add_numbers(a, b):
    return a + b

result = add_numbers(3, 7)
print("Sum:", result)"""

#64.Calculate the factorial of a number using a recursive method:
"""def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

result = factorial(5)
print("Factorial:", result)"""


#65.Check if a given string is a palindrome using a method:
"""def is_palindrome(string):
    return string == string[::-1]

result = is_palindrome("radar")
print("Is Palindrome:", result)"""

#66.Generate the Fibonacci series up to a given number of terms using a method:
"""def is_palindrome(string):
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

result = fibonacci(10)
print("Fibonacci Series:", result)"""

#67.Sort an array of integers in ascending order using a method:
"""def sort_array(arr):
    return sorted(arr)

numbers = [3, 6, 1, 9, 4, 8]
sorted_numbers = sort_array(numbers)
print("Sorted Array:", sorted_numbers)"""

#68.Reverse a given string using a method:
"""def reverse_string(string):
    return string[::-1]

result = reverse_string("Hello, World!")
print("Reversed String:", result)"""

#69.Reverse a given number using a method:
"""def reverse_number(num):
    return int(str(num)[::-1])

result = reverse_number(12345)
print("Reversed Number:", result)"""


#70.Return multiple values (minimum and maximum) using a method:
"""def min_max(arr):
    return min(arr), max(arr)

numbers = [3, 6, 1, 9, 4, 8]
min_val, max_val = min_max(numbers)
print("Minimum Value:", min_val)
print("Maximum Value:", max_val)"""


#71.Check Even or Odd:
"""def is_even(num):
    return num % 2 == 0

print(is_even(4))
print(is_even(7))"""

#72.Sum of List:
"""def is_even(num):
    return num % 2 == 0

print(is_even(4))
print(is_even(7))"""


#73.Check Prime Number:
"""def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(29))"""

#74.Convert Celsius to Fahrenheit:
"""def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(0))"""


#74.Generate Multiplication Table:
"""def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

multiplication_table(5)"""


#75.Merge Two Lists:
"""def merge_lists(lst1, lst2):
    return lst1 + lst2

print(merge_lists([1, 2, 3], [4, 5, 6]))"""


#75.Merge Two Lists:
"""def merge_lists(lst1, lst2):
    return lst1 + lst2

print(merge_lists([1, 2, 3], [4, 5, 6]))"""


#76.Check Substring::
"""def is_substring(s1, s2):
    return s1 in s2

print(is_substring("hello", "hello world"))"""


#77.math Module:
"""import math

print(math.sqrt(16))"""


#78.random Module:
"""import random

print(random.randint(1, 10))  # Output: Random integer between 1 and 10"""


#79.datetime Module:
"""import datetime

current_date = datetime.date.today()
print(current_date)  # Output: Today's date in yyyy-mm-dd format"""


#80.os Module:
"""import os

print(os.getcwd())"""

#81.Basic Syntax:
"""try:
    result = 10 / 0  # Division by zero
except ZeroDivisionError as e:
    print(f"Error: Division by zero - {e}")
else:
    print("No error occurred.")
finally:
    print("Finally block executed.")"""


#82.Multiple Except Blocks:
"""try:
    num = int(input("Enter a number: "))
    result = 10 / num  # Division by user input
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
else:
    print("No error occurred.")
finally:
    print("Finally block executed.")"""

#83.Raising Custom Exceptions:
"""try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    print(f"Error: {e}")
else:
    print("No error occurred.")
finally:
    print("Finally block executed.")"""

#84
"""class Car:
    def _init_(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.brand} {self.model} ({self.year})")

    def start_engine(self):
        print("Engine started.")

        car1 = Car("Toyota", "Camry", 2020)
        car2 = Car("Honda", "Civic", 2018)

        car1.display_info()
        car2.display_info()
        car1.start_engine()"""

#85
"""class Animal:

    def pp(self):
        print("i am super class")
    def speak(self):
        pass  

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
dog.pp()
cat.pp()"""


