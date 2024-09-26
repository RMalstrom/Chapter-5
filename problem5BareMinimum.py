"""
Richard Malstrom
CMSC-1380
This program is the bare minimum needed to solve Problem 5 on Page 103.
Date last modified: 9.26.2024
"""
import random # Import the library to generate random numbers

userTemp = int(input("Please enter the temperature you would like to convert to Celsius: "))
print(f'Your converted temperature is {(5 / 9) * (userTemp - 32)} Celsius')
