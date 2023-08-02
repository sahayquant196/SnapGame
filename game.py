import random

from deck import Deck
from player import Player


class Game(object):

    def __init__(self, deck, players):
        self.deck = deck
        self.players = players
        self.previously_drawn = None
        self.pile_size = 0

    @property
    def finished(self):
        return self.deck.is_empty()

    @property
    def winner(self):
        print( 'cards left ', self.pile_size)
        return max(self.players, key=lambda player:player.number_of_cards).player_name

    @classmethod
    def init_game(cls, number_of_packs, matching_condition):
        players = [
            Player.player_factory('Player 1'),
            Player.player_factory('Player 2'),
        ]

        deck = Deck.get_empty_deck()
        for _ in range(number_of_packs):
            deck += Deck.get_pack(matching_condition)

        deck.shuffle()

        return cls(deck, players)

    def print_state(self, drawn_card, match):
        print( 'Pile Size:{pile_size} cards_left: {cards_left}\tdrawn: {drawn_card},\tPreviously drawn: {previously_drawn_card}\tMatch: {match}\tPlayers {players}'.format(
            pile_size=self.pile_size,
            cards_left=self.deck.size(),
            drawn_card=drawn_card,
            previously_drawn_card=self.previously_drawn,
            match=match,
            players=[str(player) for player in self.players])
        )

    def turn(self):
        drawn_card = self.deck.draw()
        self.pile_size += 1

        match = False

        if self.previously_drawn is not None:
            match = drawn_card == self.previously_drawn

        if match:
            random.choice(self.players).add_pile(self.pile_size)
            self.pile_size = 0

        self.print_state(drawn_card, match)

        self.previously_drawn = drawn_card