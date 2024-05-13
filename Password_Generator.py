# Input  - N - number of passwords , Length - length of password

import re
import secrets
import string

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Generates a strong password meeting the specified criteria.

    Args:
        length (int, optional): Length of the password. Defaults to 16.
        nums (int, optional): Minimum number of digits in the password. Defaults to 1.
        special_chars (int, optional): Minimum number of special characters in the password. Defaults to 1.
        uppercase (int, optional): Minimum number of uppercase letters in the password. Defaults to 1.
        lowercase (int, optional): Minimum number of lowercase letters in the password. Defaults to 1.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If the specified criteria cannot be met.

    Examples:
        >>> generate_password()
        'P@ssw0rd1234'
        >>> generate_password(length=12, nums=2, special_chars=1)
        'P@ssw0rd12!'
    """

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_characters = letters + digits + symbols

    # Check if the specified criteria can be met
    if length < nums + special_chars + uppercase + lowercase:
        raise ValueError("The specified criteria cannot be met with the given length.")

    while True:
        password = ''
        for _ in range(length):
            password += secrets.choice(all_characters)

        # Check if the password meets the criteria
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break

    return password

    
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)