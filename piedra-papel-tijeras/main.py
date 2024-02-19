import random
import sys
class RPS:
    def __init__(self):
        print('Bienvenidos al CA CHI PUM!!!')
        self.moves: dict = {'piedra': '🗿', 'papel': '📜','tijeras': '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())

    def play_game(self):
        user_move: str = input('Piedra, papel o tijeras? \n').lower()
        if user_move == 'exit':
            print("Gracias por jugar!!")
            sys.exit()
        if user_move not in self.valid_moves:
            print("No se puede utilizar ese movimiento. No No No")
            return self.play_game()

        bot_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, bot_move)

        self.check_moves(user_move, bot_move)


    def display_moves(self, user_move: str, bot_move:str):
        print('----------------')
        print(f'Tu: {self.moves[user_move]}')
        print(f'Bot: {self.moves[bot_move]}')
        print('----------------')
    def check_moves(self, user_move: str, bot_move:str):
        if user_move == bot_move:
            print('Es\' un empate')
        elif user_move == 'roca' and bot_move == 'tijeras':
            print('Wow, ganaste!!!')
        elif user_move == 'tijeras' and bot_move == 'papel':
            print('Wow, ganaste!!!')
        elif user_move == 'papel' and bot_move == 'roca':
            print('Wow, ganaste!!!')
        else:
            print('El bot gana :(')

if __name__ == '__main__':
    rps = RPS()
    while True:
        rps.play_game()



