import random


def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls


def main():
    while True:
        try:
            user_input: str = input('Cuantas veces quieres tirar el dado?\n ')
            if user_input.lower() == 'exit':
                print('Gracias por jugar')
                break

            rolls = roll_dice(int(user_input))
            print(rolls, sep=', ')
            print(' La suma de los resultados es: ', sum(rolls))

        except ValueError:
            print('Porfavor ingrese un valor valido')


if __name__ == '__main__':
    main()
