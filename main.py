# password generator mini project

import string
import random


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    condition = False  # meets criteria has a number or special character
    has_number = False
    has_special = False

    while not condition or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True

        condition = True
        if numbers:
            condition = has_number
        if special_characters:
            condition = condition and has_special

    return pwd


pwd = generate_password(8)
print(pwd)
