"""
# 🟢 Exercises — Easy → Hard
# Exercise 1 — Name
# Ask the user for their name and print:
# Hello, John!
name = input ("Enter your name: ")
print (f"Hello, {name}")

# Exercise 2 — Age
# Ask the user for their age and print:
# You are 24 years old.
# Convert the input to an integer.

age = int (input("Enter your age: "))
print (f"You are {age} years old.")

# Exercise 3 — Country

# Ask for the user's country and print:

# You live in Malaysia.

country = input ( "Where do you live ? ")
print(f"You live in {country}")

# Exercise 4 — Two Numbers
# Ask the user for two numbers and print their sum.
# Example:
# Enter first number: 10
# Enter second number: 5
# Sum: 15
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
sum = number1 + number2
print (f"First  number:    {number1}")
print (f"First number:     {number2}")
print (f"Sum of 2 numbers: {sum}")


# Exercise 5 — Rectangle

# Ask the user for:

# length
# width

# Convert them to integers and calculate the area.

# Example:

# Length: 10
# Width: 5
# Area: 50

length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
print (f"Length: {length}")
print (f"Width:  {width}")
print (f"Area:   {area}")

# Exercise 6 — Age in 5 Years
# Ask the user's current age.
# Print their age 5 years from now.
# Example:
# Current age: 24
# Age in 5 years: 29
age = int (input("Enter your current age: "))
print (f"Current age:    {age}")
print (f"Age in 5 years: {age + 5}")


# Exercise 7 — Shopping Total
# Ask the user for:
# product price
# quantity
# Calculate:
# Total = price × quantity
# Use float() for the price and int() for quantity.

product_price = float(input( "Enter the product price: "))
quantity = int (input ("Enter the quantity: "))
total = product_price * quantity
print(f"Product price: {product_price}")
print(f"Quantity:      {quantity}")
print(f"Total:         {total}")
"""


# Exercise 8 — Average

# Ask the user for three exam marks:

# Math
# Programming
# English

# Calculate and print the average.

# Example:

# Math: 80
# Programming: 90
# English: 70

# Average: 80.0
math = float(input("What is your exam marks for math: "))
programming = float(input("What is your exam marks for programming: "))
english = float(input("What is your exam marks for english: "))
average = (math + programming + english)/3
print(F"Math:        {math   }")
print(F"Programming: {programming   }")
print(F"English:     {english   }")
print(F"Average:     {average   }")




# Exercise 9 — Personal Profile

# Ask the user for:

# name
# age
# country
# university
# course

# Then print a profile like:

# ========== PROFILE ==========

# Name: John
# Age: 24
# Country: Malaysia
# University: ABC University
# Course: Computer Science
# 🔴 Exercise 10 — Challenge: Receipt

# Ask the user for:

# product
# price
# quantity
# discount

# Convert the appropriate values and calculate:

# Subtotal = price × quantity
# Discount = subtotal × discount
# Final Price = subtotal - discount

# Example:

# Product: Laptop
# Price: 3000
# Quantity: 2
# Discount: 0.15

# Expected:

# ========== RECEIPT ==========

# Product: Laptop
# Price: 3000
# Quantity: 2
# Subtotal: 6000
# Discount: 900.0
# # Final Price: 5100.0