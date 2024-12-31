from cards.deck import Deck
from cards.card import Card


class MockDeck(Deck):
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def load(self, card: Card) -> None:
        self.cards.append(card)
