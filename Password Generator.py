import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    
    digits = string.digits
    special_characters = string.punctuation
    
    all_characters = lowercase + uppercase + digits + special_characters
    password = random.choices(all_characters, k=length)
    
    random.shuffle(password)
    return ''.join(password)

length = int(input("Enter the desired length of the password: "))
password = generate_password(length)
print("Generated Password:- ", password)
