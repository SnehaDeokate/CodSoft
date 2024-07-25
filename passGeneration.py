import random
import string

def generate_password(length):
    # Define the character sets to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 1:
                print("Password length must be at least 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Generate and display the password
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
