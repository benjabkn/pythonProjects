import itertools
import string
import time

def load_word_list(file_path: str) -> list[str]:
    try:
        with open(file_path, 'r', encoding='latin1') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f'Error: No se pudo encontrar el archivo {file_path}')
        return []

def common_guess(word: str, word_list: list[str]) -> str | None:
    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f'Coincidencia común: {match} (#{i})'

def brute_force(word: str, length: int, digits: bool = False, symbols: bool = False) -> str | None:
    chars: str = string.ascii_lowercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess_str: str = ''.join(guess)
        if guess_str == word:
            return f'{word} fue crackeada en {attempts:,} intentos'
    return None

def main():
    print('Buscando...')
    password: str = 'benja1234'
    word_list: list[str] = load_word_list('words.txt')

    start_time: float = time.perf_counter()
    if common_match := common_guess(password, word_list):
        print(common_match)
    else:
        for length in range(1, len(password) + 1):
            if cracked := brute_force(password, length, digits=True, symbols=False):
                print(cracked)
                break
        else:
            print("No se encontró coincidencia")
    end_time: float = time.perf_counter()
    print(f'Tiempo total: {round(end_time - start_time, 2)} segundos')

if __name__ == '__main__':
    main()
