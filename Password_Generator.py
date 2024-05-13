# Input  - N - number of passwords , Length - length of password

# Method-1 using Regex and Secrets Module - More sophisticated
import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password
    
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)




# Method-2 : More of a basic approach
# Learn about random here

import random
print('Welocme : How may the Password Generator Help You')

# Contains symbols, 0-9, a-z, A-Z
chars = "ibsdcihscbhakus9883eewu920ej\[s[SX;Lahx-9q-9d08qe98d180-1d,m lamkaj ubq-0\]"

num = input("ENTER LENGTH OF YOUR PASSWORD: ")

password =''
for i in range(int(num)):
    password += random.choice(chars)

print('\n here is your password: ' + password)


