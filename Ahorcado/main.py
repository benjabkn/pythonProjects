from random import choice


def run_game():
    word: str = choice(['manzana', 'secret', 'banana', 'minion'])
    username: str = input('Cual es tu usuario >> ')
    print(f'Bienvenido al ahorcado, {username}')

    tries: int = 3
    letters: int > 3
    guessed: str = ''
    while tries > 0:
        blanks: int = 0
        print('  Word:       \n', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print(' _', end='')
                blanks += 1
        print()
        if blanks == 0:
            print(' Lo lograste !!! ')
            break

        guess: str = input('Enter a letter: ')
        if guess in guessed:
            print(f'Ya usaste la palabra {guess}, prueba con otra!')
            continue

        guessed += guess
        if guess not in word:
            tries -= 1
            print(f'Te equivocaste, tienes {tries}hp restante.')

            if tries == 0:
                print('No tienes mas vida :c \n eres un perdedor.')

            # Setup


if __name__ == '__main__':
    run_game()
