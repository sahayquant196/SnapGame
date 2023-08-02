import random

from Consts import Match_Cond, Values, Suits


class Deck(object):

    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def is_empty(self):
        return len(self.cards) == 0

    def size(self):
        return len(self.cards)

    def __iadd__(self, other):
        self.cards += other.cards
        return self

    @classmethod
    def get_empty_deck(cls):
        return cls([])

    @classmethod
    def get_pack(cls, matching_condition):
        card_class = Match_Cond[matching_condition]

        cards = []
        for value in Values:
            for suit in Suits:
                cards.append(card_class(value, suit))

        return cls(cards)

    def __str__(self):
        return str([str(card) for card in self.cards])