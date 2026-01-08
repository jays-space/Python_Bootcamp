import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


def generate_letters(nof_letters):
    generated_letters = []
    for i in range(0, nof_letters):
        generated_letters.append(random.choice(letters))

    return generated_letters

def generate_symbols(nof_symbols):
    generated_symbols = []
    for i in range(0, nof_symbols):
        generated_symbols.append(random.choice(symbols))

    return generated_symbols

def generate_numbers(nof_numbers):
    generated_numbers = []
    for i in range(0, nof_numbers):
        generated_numbers.append(random.choice(numbers))

    return generated_numbers

def generate_password(nof_letters, nof_symbols, nof_numbers):
    joined_password = []
    password = ""
    separator = ''

    joined_password.extend(generate_letters(nof_letters))
    joined_password.extend(generate_symbols(nof_symbols))
    joined_password.extend(generate_numbers(nof_numbers))

    random.shuffle(joined_password)
    password += separator.join(joined_password)

    return password


print(generate_password(nr_letters, nr_symbols, nr_numbers))