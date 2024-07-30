import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")

    # Define the character pools
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Make sure the password includes at least one character from each pool
    password_chars = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all pools combined
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password_chars += random.choices(all_characters, k=length-4)

    # Shuffle to prevent any predictable patterns
    random.shuffle(password_chars)

    # Join the list into a string
    password = ''.join(password_chars)
    return password

# Example usage
password_length = 12
password = generate_password(password_length)
print(f"Generated password: {password}")