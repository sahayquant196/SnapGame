class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '{suit} {value}'.format(suit=self.suit, value=self.value)


class CardValue(Card):
    def __init__(self, *args, **kwargs):
        super(CardValue, self).__init__(*args, **kwargs)

    def __eq__(self, other):
        return self.value == other.value


class CardSuit(Card):
    def __init__(self, *args, **kwargs):
        super(CardSuit, self).__init__(*args, **kwargs)

    def __eq__(self, other):
        return self.suit == other.suit


class CardSuitOrValue(Card):
    def __init__(self, *args, **kwargs):
        super(CardSuitOrValue, self).__init__(*args, **kwargs)

    def __eq__(self, other):
        return self.value == other.value or self.suit == other.suit