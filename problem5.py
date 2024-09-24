'''
Richard Malstrom
CMSC-1380

This program takes a users input of a temperature and if it is Celsius or Fahrenheit
'''

userTemp = int(input("Please enter your temperature you would like to convert ")) # Take the user input of their temperature
userType = input("Is this temperature in Celsius or Fahrenheit: C/F ") # Take user input of what unit the temperature is currently in

if userType.upper() == "F": # If the temperature is already in Fahrenheit, we need to convert it to Celsius
    convertedTemp =  (userTemp - 32) / (9/5)
    tempUnit = "Celsius" # Used to call back when printing out the users final answer
else: # If temperature is already in Celsius, we need to convert it to Fahrenheit
    convertedTemp = userTemp * 9/5 + 32
    tempUnit = "Fahrenheit" # Used to call back when printing out the users final answer
    
print(f'Your converted temp is {convertedTemp} {tempUnit}') # Print out the users final answer
