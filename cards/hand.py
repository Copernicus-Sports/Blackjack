from __future__ import annotations

from cards.card import Card

from enum import Enum


class HandType(Enum):
    SOFT = "SOFT"
    HARD = "HARD"


class Hand:
    def __init__(self) -> None:
        self.value = 0
        self.type = HandType.HARD
        self.bet = 1

        self.cards: list[Card] = []

    def __repr__(self) -> str:
        return f"{self.type.value} {self.value} : {self.cards}"

    def double(self) -> None:
        self.bet *= 2

    def add(self, card: Card) -> None:
        if self.is_bust():
            return

        self.value += card.value

        if card == Card.ACE and self.type == HandType.HARD:
            self.type = HandType.SOFT

        if self.is_bust() and self.type == HandType.SOFT:
            self.value -= 10
            self.type = HandType.HARD

        self.cards.append(card)

    def split(self) -> tuple[Hand, Hand]:
        if not self.is_pair():
            raise AssertionError(
                f"Attempted to split hand that is not a pair: {self}"
            )

        hand_lhs, hand_rhs = Hand(), Hand()

        hand_lhs.add(self.cards[0])
        hand_rhs.add(self.cards[1])

        return hand_lhs, hand_rhs

    def is_pair(self) -> bool:
        return len(self.cards) == 2 and self.cards[0] == self.cards[1]

    def is_bust(self) -> bool:
        return self.value > 21

    def is_blackjack(self) -> bool:
        return self.value == 21 and len(self.cards) == 2


class HandEvaluator:
    @staticmethod
    def evaluate(player_hand: Hand, dealer_hand: Hand) -> float:
        multiplier: float = 0.0

        if player_hand.is_blackjack() and not dealer_hand.is_blackjack():
            multiplier = 1.5

        elif player_hand.value > dealer_hand.value:
            multiplier = 1

        elif player_hand.value < dealer_hand.value:
            multiplier = -1

        return multiplier * player_hand.bet
