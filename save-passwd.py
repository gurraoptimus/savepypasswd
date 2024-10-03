# Author: Gurraoptimus
# Date: 24-10-3
# Description: This script generates a random password and saves it to a file.

import random
import string

# Function definitions follow...

def generate_password(length=12):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_random_filename(extension=".txt", length=8):
    # Generate a random filename with specified length and extension
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return f"{random_chars}{extension}"

def save_password_to_file(password, filename):
    with open(filename, 'w') as file:
        file.write(password)
    return filename  # Return the filename for later use

if __name__ == '__main__':
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    filename = generate_random_filename()  # Generate a random filename
    save_password_to_file(password, filename)  # Store the filename
    print(f"Generated password: {password}")
    print(f"Password saved to {filename}.")
