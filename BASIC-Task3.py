import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyz"
    password = ""

    for i in range(length):
        next_char_index = random.randrange(len(characters))
        password += characters[next_char_index]

    password = add_digit(password)
    password = add_capital_letter(password)

    return password

def add_digit(word):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(word)//2)
        word = word[0:replace_index] + str(random.randrange(10)) + word[replace_index+1:]
    return word

def add_capital_letter(word):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(word)//2, len(word))
        word = word[0:replace_index] + word[replace_index].upper() + word[replace_index+1:]
    return word

def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(num_passwords) + " passwords")

    password_lengths = []

    print("Minimum password length is 3")

    for i in range(num_passwords):
        length = int(input("How long should Password #" + str(i+1) + " be? "))
        if length < 3:
            length = 3
        password_lengths.append(length)

    passwords = []

    for length in password_lengths:
        passwords.append(generate_password(length))

    for i, password in enumerate(passwords):
        print("Password #" + str(i+1) + " is " + password)

if __name__ == "__main__":
    main()
