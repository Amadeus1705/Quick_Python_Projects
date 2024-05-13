# Luhn Algorithm Implementation

# 1. Double Every Other Digit:
#    - Starting from the rightmost digit, double the value of every second digit.

# 2. Adjust Large Digits:
#    - If doubling a digit results in a number greater than 9, sum the digits of the products.

# 3. Sum All Digits:
#    - Add up all the digits, both the original and the adjusted doubled digits.

# 4. Check for Divisibility by 10:
#    - If the total sum is divisible by 10, the number is valid (including its check digit).
#    - Otherwise, the number is invalid.


# Example: Validating Account Number "7992739871"

# Account Number:      7   9   9   2   7   3   9   8   7   1   x 
# Double Every Other:  7  18   9   4   7   6   9  16   7   2   x
# Sum 2-Digit Numbers: 7   9   9   4   7   6   9   7   7   2   x

# Total Sum: 67 + x
# Check Digit (x) = 3  (to make the sum divisible by 10)

# Valid Account Number: 79927398713 

def verify_card_number(card_number):
    """
    Verifies the validity of a credit card number using the Luhn algorithm.

    Args:
        card_number: The credit card number to be verified.

    Returns:
        True if the card number is valid, False otherwise.
    """

    # 1. Double Every Other Digit:
    #    - Starting from the rightmost digit, double the value of every second digit.
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # 2. Adjust Large Digits:
    #    - If doubling a digit results in a number greater than 9, sum the digits of the products.
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    # 3. Sum All Digits:
    #    - Add up all the digits, both the original and the adjusted doubled digits.
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)

    # 4. Check for Divisibility by 10:
    #    - If the total sum is divisible by 10, the number is valid (including its check digit).
    #    - Otherwise, the number is invalid.
    return total % 10 == 0

def main(input_card_num):
    """
    Takes a credit card number as input and prints whether it's valid or invalid.

    Args:
        input_card_num: The credit card number to be verified.
    """
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

card_number = '7992-7398-713'
main(card_number) 