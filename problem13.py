"""
Richard Malstrom
CMSC-1380

This code will simulate rolling 2 dice using random number generation.

Date last modified: 9.24.2024
"""

import random # Import the 'random' library

dice1 = random.randint(1,6) # Create a random number for the first die
dice2 = random.randint(1,6) # Create a random number for the second die

# Print out the results to the user
print(f'Your dice rolled {dice1} and {dice2}')
print(f'Total roll is {dice1 + dice2}')
