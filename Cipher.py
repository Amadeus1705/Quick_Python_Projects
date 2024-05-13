def vigenere(message, key, direction=1):
    """
    Encrypts or decrypts a message using the Vigenère cipher.

    Args:
        message (str): The text to encrypt or decrypt.
        key (str): The keyword used for encryption/decryption.
        direction (int): 1 to encrypt, -1 to decrypt (default is 1).

    Returns:
        str: The encrypted or decrypted message.
    """
    
    key_index = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_message = ""

    for char in message.lower():
        if not char.isalpha():  # Skip non-alphabetic characters
            final_message += char
        else:
            key_char = key[key_index % len(key)]  # Cycle through the key
            key_index += 1 

            offset = alphabet.index(key_char)      # Find the numerical shift value
            index = alphabet.find(char)           # Find the numerical index of the letter
            
            # Calculate the new index (wrapping around the alphabet if needed)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message


def encrypt(message, key):
    """
    Encrypts a message using the Vigenère cipher.

    Args:
        message (str): The text to encrypt.
        key (str): The keyword used for encryption.

    Returns:
        str: The encrypted message.
    """
    return vigenere(message, key, 1)


def decrypt(message, key):
    """
    Decrypts a message using the Vigenère cipher.

    Args:
        message (str): The text to decrypt.
        key (str): The keyword used for decryption.

    Returns:
        str: The decrypted message.
    """
    return vigenere(message, key, -1)

# Main Input/Output
text = input("Enter your message: ")  # Get the message to encrypt/decrypt
custom_key = input("Enter your key: ") 

# Encryption/Decryption Choice
while True:  # Loop until valid choice is entered
    choice = input("Do you want to encrypt (e) or decrypt (d)? ").lower()
    if choice in ('e', 'd'):
        break
    else:
        print("Invalid choice. Please enter 'e' or 'd'.")

if choice == 'e':
    result = encrypt(text, custom_key)
    print("Encrypted message:", result)
else:
    result = decrypt(text, custom_key)
    print("Decrypted message:", result)
