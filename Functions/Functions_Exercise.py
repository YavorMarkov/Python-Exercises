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

# Call the function 'make
