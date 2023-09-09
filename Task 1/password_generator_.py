import string
import random

letters = string.ascii_letters
symbols = "()!@#$%_+-"
digits = string.digits
characters = symbols + letters + digits
check = True

password = ""


def generate_password(length):
    return password.join(random.sample(characters, length))


while check:
    user_input = input("Enter password length: ")

    if user_input.isdigit():
        result = generate_password(int(user_input))
        print(f"\nYour Password is: {result}")
        check = False
    else:
        print("Length must be a digit \n")
