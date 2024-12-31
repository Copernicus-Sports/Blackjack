from cards.card import Card
from random import shuffle


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

        for card in Card:
            for _ in range(4):
                self.cards.append(card)

        self.shuffle()

    def __repr__(self) -> str:
        return str(self.cards)

    def shuffle(self) -> None:
        shuffle(self.cards)

    def empty(self) -> bool:
        return len(self.cards) == 0

    def deal(self) -> Card:
        try:
            return self.cards.pop(0)
        except IndexError:
            raise IndexError("Tried to deal from an empty deck")
