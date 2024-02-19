from random import randint

lower_num, higher_num = 0, 100
random_number: int = randint(lower_num, higher_num)
print(f'Ahora adivina el numero en un rango de {lower_num} y {higher_num}, cada vez que falles, el sistema indicará una pista de su valor. Suerte')


while True:
    try:
        user_guess: int = int(input("Ingresa un numero: "))
    except ValueError as e:
        print('Porfavor ingresa un numero valido.')
        continue
    if user_guess > random_number:
        print("El numero es menor")
    elif user_guess < random_number:
        print("El numero es mayor")
    else:
        print("Adivinaste uwu!!! wow ")
        break

