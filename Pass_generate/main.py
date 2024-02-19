import string
import secrets

def contains_upper(password: str)-> bool:
    for char in password:
        if char.isupper():
            return True

    return False

def contains_symbols(password: str)-> bool:
    for char in password:
        if string.punctuation:
            return True

    return False

def generate_pass(length: int, symbols: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits
    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_lowercase
    combination_length = len(combination)
    new_pass : str = ''
    for _ in range(length):
        new_pass += combination[secrets.randbelow(combination_length)]

    return new_pass

if __name__ == '__main__':
    for i in range(1, 6):
        new_pass: str = generate_pass(length=20, symbols=True, uppercase=False)
        specs: str = f'uppercase: {contains_upper(new_pass)}, symbols: {contains_symbols(new_pass)}'
        print(f'Constreña: {i}---> \n', new_pass)
