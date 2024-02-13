import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Asking the user for the number of letters, symbols, and numbers
nr_letters = int(input("How many letters would you like in your password?\n")) 
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

# Asking the user whether they want an easy or hard password
password_difficulty = input("Would you like an easy password or a hard one ? Type 'easy' or 'hard': ").lower()

# Generating random letters
random_letters = []
for _ in range(nr_letters):
    random_letters.append(random.choice(letters))

# Generating random symbols
random_symbols = []
for _ in range(n_symbols):
    random_symbols.append(random.choice(symbols))

# Generating random numbers
random_numbers = []
for _ in range(n_numbers):
    random_numbers.append(random.choice(numbers))

# Concatenating all random characters to form a password list
password_list = random_letters + random_symbols + random_numbers

# Concatenating all characters to form a password
password = ''.join(password_list)

# Printing the password based on user preference
if password_difficulty == 'easy':
    print("Your easy password:", password)
else:
    # Shuffling the password list for hard difficulty
    random.shuffle(password_list)
    hard_password = ''.join(password_list)
    print("Your hard password(No geek can hack it -ç-):", hard_password)
