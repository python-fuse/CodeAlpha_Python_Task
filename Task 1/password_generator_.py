# Import necessary libraries
import string   # Import the 'string' module for character sets
import random   # Import the 'random' module for randomization

# Define character sets for generating passwords
letters = string.ascii_letters  # Uppercase and lowercase letters
symbols = "()!@#$%_+-"         # Common symbols for passwords
digits = string.digits          # Digits (0-9)

characters = symbols + letters + digits  # Combine all characters into one list

check = True   # Flag for user input validation
password = ""  # Initialize an empty password string

# Function to generate a random password of a specified length
def generate_password(length):
    return password.join(random.sample(characters, length))

# Loop to repeatedly prompt the user for password length until valid input is provided
while check:
    user_input = input("Enter password length: ")

    if user_input.isdigit():  # Check if the input is a digit
        result = generate_password(int(user_input))  # Generate the password
        print(f"\nYour Password is: {result}")  # Print the generated password
        check = False  # Exit the loop since valid input was provided
    else:
        print("Length must be a digit \n")  # Prompt the user for valid input
