from utils import inputs_from_user

from game import Game


if __name__ == '__main__':
    number_of_packs, matching_condition = inputs_from_user()
    game = Game.init_game(number_of_packs, matching_condition)

    while not game.finished:
        game.turn()
    print('\n')
    print('The winner is....' + game.winner)
    print('Congratulations!')
