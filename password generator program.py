# import the random module
import random

# define the characters that can be used in the password
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()-_=+[]{};:,.<>/?\\|"

# define the minimum and maximum length of the password
min_length = 8
max_length = 16

# define a function to generate a random password
def generate_password():
    # choose a random length between the minimum and maximum
    length = random.randint(min_length, max_length)
    # create an empty string to store the password
    password = ""
    # loop until the password reaches the desired length
    while len(password) < length:
        # choose a random character type
        char_type = random.choice(["lowercase", "uppercase", "digits", "symbols"])
        # choose a random character from the corresponding type
        if char_type == "lowercase":
            char = random.choice(lowercase)
        elif char_type == "uppercase":
            char = random.choice(uppercase)
        elif char_type == "digits":
            char = random.choice(digits)
        else:
            char = random.choice(symbols)
        # append the character to the password
        password += char
    # return the password
    return password

# test the function
print("Your password is:", generate_password())
