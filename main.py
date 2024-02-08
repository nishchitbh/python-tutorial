# Data type
# Number: Integer, float
number = 5  # Integer
data = 5269.9  # float data type
unknown = 'my name is nishchit'  # string datatype
subjects = ["Physics", "Chemistry", "Maths",
            "Nepali", "Maths"]  # List datatype
tuples = (1,3,4)
subject_set = {"Physics", "Chemistry", "Maths", "Maths"}  # Set datatype
dictionary = {
    'Book': 'A set of pages with written information',
    'Computer': 'A device',
    'School': 'A place to study'
}  # Dictionary
boolean = True  # Boolean Data types

# Integer/Float operations
sum = 5+9  # Output -> 14
difference = 5-9  # Output -> -4
multiplication = 5*9  # Output -> 45
division = 5/9  # Output -> .5556
exponential = 5**2  # Output -> 25
mod = 5 % 2  # Remainder of 5 when divided by 2 --> 1

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
vegetables = ['potato', 'tomato', 1, ['hello']]
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

# Comparison operators
a = 2
b = 3
c = 6
print(a > b)  # True
print(b > c)  # False
print(a != b)  # <- Not equals -> True
print(a > b and a > c)  # False
print(a > b or a > c)  # True
print('potato' in vegetables)  # True
print('banana' in vegetables)  # False
print('banana' not in vegetables)  # True

# Conditional Statement
# If else
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")
    

# Match case
roll_no = int(input("Enter roll number: "))
match roll_no:
    case 1:
        print("Nishchit")
    case 2:
        print("Diwash")
    case 3:
        print("Mandeep")

# Loops
# For loop
for i in range(50):
    print(i)
    if i==27:
        break
else:
    print('loop not broken')
for i,j in enumerate(vegetables):
    print(f'position {i}')
    print(f'element: {j}')

# While loop
c = 0
while c<10:
    print(c)
    c+=1
    if c==5:
        break
else:
    print('loop not broken')
    
def area_of_rectangle(l,b):
    
    return(l*b)
l1 = 5
b1 = 3
l2 = 7
b2 = 4
print(area_of_rectangle(l1,b1))
print(area_of_rectangle(l2,b2))

# Functions
def area(l,b):
    return l*b

l1 = 5
b1 = 3


# Use of map
def capitalization(word):
    return word.capitalize()
students = ['nishchit','diwash','mandeep']

students_capitalized = list(map(capitalization, students))
print(students_capitalized)