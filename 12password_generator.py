import random 
import string

def generate_password(length, numbers = True, symbols = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    password = []
    if numbers:
        password.append(random.choice(digits))
    if symbols:
        password.append(random.choice(special))

    all_char = letters
    if numbers:
        all_char += digits
    if symbols:
        all_char += special

    while len(password) < length:
        password.append(random.choice(all_char))

    random.shuffle(password)

    return "".join(password)

max_length = int(input("Enter max length of password: "))
has_number = input("Do you want add a number? (Y/N): ").lower() == "y"
has_symbols = input("Do you want add a symbols? (Y/N): ").lower() == "y"

min_required = 0
if has_number:
    min_required += 1
if has_symbols:
    min_required += 1

if max_length < min_required:
    print(f"Password must be at least {min_required} characters long.")
else:
    code = generate_password(max_length, has_number, has_symbols)
    print(code)


