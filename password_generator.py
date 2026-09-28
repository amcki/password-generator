import random
import string


def generate_password(length):
    # string.ascii_letters = a-z and A-Z
    # string.digits = 0-9
    # string.punctuation = symbols like !@#$%
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=== Password Generator ===")
    length = int(input("How long should the password be? "))
    password = generate_password(length)
    print(f"Your password is: {password}")


if __name__ == "__main__":
    main()