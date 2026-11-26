import random
import string

def generate(length=12, symbols=True, digits=True):
    chars = string.ascii_letters
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation
    return "".join(random.SystemRandom().choice(chars) for _ in range(length))

length = int(input("Password length: "))
use_symbols = input("Include symbols? (y/n): ").lower() == "y"
use_digits = input("Include digits? (y/n): ").lower() == "y"
print("Your password:", generate(length, use_symbols, use_digits))
