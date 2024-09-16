import random
import string

def generate_password(length):
    """Generate a random password of specified length."""
    # Define the character sets to use
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    while True:
        try:
            # Prompt the user for the desired password length
            length = int(input("Enter the desired length of the password: "))
            
            # Validate the input
            if length <= 0:
                print("The length must be a positive integer.")
                continue
            
            # Generate and display the password
            password = generate_password(length)
            print(f"Generated Password: {password}")
            break
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
