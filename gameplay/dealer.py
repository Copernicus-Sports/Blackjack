from cards.deck import Deck
from gameplay.rules import Rules
from cards.hand import Hand, HandType


class Dealer:
    def __init__(self, deck: Deck, rules: list[Rules]) -> None:
        self.deck = deck
        self.rules = rules

        self.hand = Hand()
        self.upcard = self.deck.deal()
        self.hand.add(self.upcard)

    def play(self) -> Hand:
        while not self.hand.is_bust():
            card = self.deck.deal()
            self.hand.add(card)

            if (
                self.hand.value > 17
                or (self.hand.value == 17 and self.hand.type == HandType.HARD)
                or (self.hand.value == 17 and not self.hit_soft_seventeen())
            ):
                break

        return self.hand

    def hit_soft_seventeen(self) -> bool:
        return Rules.DEALER_HIT_SOFT_SEVENTEEN in self.rules
