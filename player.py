class Player(object):
    def __init__(self, number_of_cards, player_name):
        self.number_of_cards = number_of_cards
        self.player_name = player_name

    @classmethod
    def player_factory(cls, player_name):
        return cls(0, player_name)

    def add_pile(self, number_of_cards):
        self.number_of_cards += number_of_cards

    def __str__(self):
        return '{name} {pile}'.format(name=self.player_name, pile=self.number_of_cards)