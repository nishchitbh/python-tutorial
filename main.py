# Data type
# Number: Integer, float
import numpy as np

number = 5 # Integer
data = 5269.9 # float data type
unknown =  'my name is nishchit'# string datatype
subjects = ["Physics", "Chemistry","Maths","Nepali", "Maths"] # List datatype
subject_set = {"Physics","Chemistry","Maths","Maths"} #Set datatype
dictionary = {
    'Book': 'A set of pages with written information',
    'Computer': 'A device',
    'School': 'A place to study'
    } # Dictionary
boolean = True #Boolean Data types

# Integer/Float operations
sum = 5+9 # Output -> 14
difference = 5-9 # Output -> -4
multiplication = 5*9 # Output -> 45
division = 5/9 # Output -> .5556
exponential = 5**2 # Output -> 25
mod = 5%2 # Remainder of 5 when divided by 2 --> 1

# String operations 
string = "Hello"
print(len(string)) # Output -> 5
print(string[0]) # Output -> H
print(string[1]) # Output -> e
print(string[-1]) # Output -> o
print(string[1:4]) # Output -> ell
print(string.upper()) # Output -> HELLO
print(string.lower()) # Output -> hello
print(string.capitalize()) #Output -> Hello

# List operations
vegetables = ['potato','tomato', 1, ['hello']]
print(vegetables[0]) # Output -> Potato
print(vegetables[-1]) # Output -> ['hello']
vegetables.append('cauliflower')
vegetables.extend(subjects)
vegetables.remove('Maths')
vegetables.insert(7, 'Maths')
print(vegetables)

# Dictionary Operations 
print(len(dictionary)) # Output -> 3
print(list(dictionary.keys())) # Output -> ['Book', 'Computer', 'School']
print(list(dictionary.values())) # Output -> ['A set of pages with written information', 'A device', 'A place to study']


# Loop
