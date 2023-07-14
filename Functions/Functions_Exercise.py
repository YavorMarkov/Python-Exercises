#  example 1:
def greet(name):
    print(f"Hello {name}" )
greet("Yavor") # Output: Hello, Alice!

# example 2:
#Return Value
def add_numbers(num1, num2):
    return num1 + num2 
sum = add_numbers(3, 4)
print(sum) #Output 7

# example 3:
# Default Values
def greet(name='world'):
    print(f"Hello, {name}!")

greet() # Output: Hello world!
greet("Yavor") #Output, hello Yavor"n  

# Example 4 
# Arbitrary Number of Arguments 

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Example 4 with explanations
# Arbitrary Number of Arguments 

# Define the function 'make_pizza' that can take an arbitrary number of arguments
def make_pizza(*toppings):
    # Print a message about making a pizza
    print("\nMaking a pizza with the following toppings:")

    # Iterate over each item in the 'toppings' tuple
    for topping in toppings:
        # Print the current topping
        print(f"- {topping}")

# Call the function 'make_pizza' with one topping
make_pizza('pepperoni')

# Call the function 'make_pizza' with three toppings
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# example 5
# Keyword Arguments

#Keyword arguments allow you to specify a name-value pair for arguments. 
#This way, the order of arguments doesn't matter:

def describe_pet(pet_name, animal_type='dog'):
    print(f"\nLI have a {animal_type}. ")
    print(f"My {animal_type}'s name is {pet_name}. ")

describe_pet(pet_name='Willie')
describe_pet(animal_type='hamster', pet_name='Harry')

# example 5 with explanations
# Keyword Arguments
# Define a function called describe_pet that takes two parameters: 
# pet_name (required) and animal_type (optional with default value 'dog')
def describe_pet(pet_name, animal_type='dog'):
    # Print a statement about the type of pet
    print(f"\nI have a {animal_type}.")
    # Print a statement about the pet's name
    print(f"My {animal_type}'s name is {pet_name}.")

# Call the function describe_pet with 'pet_name' parameter as 'Willie'.
# The 'animal_type' parameter is not provided, so it uses the default value 'dog'
describe_pet(pet_name='Willie')

# Call the function describe_pet with both parameters provided,
# 'animal_type' as 'hamster' and 'pet_name' as 'Harry'
describe_pet(animal_type='hamster', pet_name='Harry')

"""This code demonstrates the use of default parameters in Python. 
In this case, the animal_type parameter has a default value of 'dog', 
which means that if no value is provided for animal_type when describe_pet is called, 
Python will use the value 'dog'. In the second function call, the animal_type is provided explicitly, 
so the default value is ignored."""

# Example 5 Recursive Functions
# In Python, a function can call itself, which is known as a recursive function. 
# Recursion is a common mathematical and programming concept. 
# It means that a function calls itself, so it loops until it gets a result.

# For example, a classic use case of recursion is to calculate factorials:

def factorial(n):
    if n == 1:
        return 1
    else: 
        return n * factorial(n-1)
print(factorial(5)) #Outputs: 120 


#  Example 6 Lambda Functions
'''Lambda functions are small, anonymous functions that are defined with the lambda keyword, 
and can be used wherever function objects are required. 
They are syntactically restricted to a single expression.'''

square = lambda x: x ** 2
print(square(5)) # Output 25

# Example 7 The map() Function
# map() is a function that takes in two or more arguments: a function and one or more iterables. 
# In Python 2, it returns a list of the results after applying the given function to each item of a given iterable. 
# In Python 3, it returns a map object which is an iterator.

number = [1,2,3,4,5]
squared = map(lambda x: x**2, numbers)
print(list(squared)) # Outputs [1, 4, 9, 16 ,25 ]

# Example 7 with explanations Lambda Functions

# Define a list named 'numbers' containing the integers from 1 to 5
numbers = [1, 2, 3, 4, 5]

# Use the built-in 'map' function to apply a function to every item in 'numbers'
# The function is specified with a lambda expression, which defines an anonymous function
# The lambda function takes an argument 'x' and returns 'x' squared (x**2)
# 'map' returns an iterable object, so it needs to be converted to a list to print the values
squared = map(lambda x: x**2, numbers)

# Convert the map object 'squared' to a list and print the result
# The result is a list of the squares of the numbers in the original 'numbers' list
print(list(squared))  # Outputs: [1, 4, 9, 16, 25]


# example 8 The filter() Function
# filter() constructs an iterator from elements of an iterable for which a function returns true.
# In this example, the filter() function iterates over each element in the numbers list 
# and applies the lambda function, which checks if a number is even.
# Only the numbers for which the lambda function returns True are included in the new list.````

numbers = [1, 2, 4, 5]
filtered = filter(lambda x: x % 2 == 0, numbers)
print(list(filtered)) # Output [2,4]