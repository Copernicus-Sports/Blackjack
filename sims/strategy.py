from enum import Enum

from cards.hand import Hand, HandType
from cards.card import Card


class Decision(Enum):
    HIT = "HIT"
    STAND = "STAND"
    DOUBLE = "DOUBLE"
    SPLIT = "SPLIT"
    SURRENDER = "SURRENDER"


class Strategy:
    def __init__(self) -> None:
        self.hard_hands: dict[tuple[int, Card], Decision] = {}
        self.soft_hands: dict[tuple[int, Card], Decision] = {}
        self.pairs: dict[tuple[Card, Card], Decision] = {}

    def decide(self, hand: Hand, dealer_upcard: Card) -> Decision:
        if hand.is_pair():
            return self.pairs[(hand.cards[0], dealer_upcard)]
        elif hand.type == HandType.SOFT:
            return self.soft_hands[(hand.value, dealer_upcard)]
        else:
            return self.hard_hands[(hand.value, dealer_upcard)]
