from cards.deck import Deck
from cards.hand import Hand
from cards.card import Card

from sims.strategy import Strategy, Decision


class Player:
    def __init__(self, deck: Deck, strategy: Strategy) -> None:
        self.deck = deck
        self.strategy = strategy

    def play(self, hand: Hand, dealer_upcard: Card) -> list[Hand]:
        hands: list[Hand] = []

        while True:
            first_decision = self.strategy.decide(hand, dealer_upcard)

            match first_decision:
                case Decision.DOUBLE:
                    hand.double()
                    hands.append(self._play_hand(hand, dealer_upcard))

                case Decision.SPLIT:
                    hand_lhs, hand_rhs = hand.split()

                    hand_lhs.add(self.deck.deal())
                    hand_rhs.add(self.deck.deal())

                    hands += self.play(hand_lhs, dealer_upcard)
                    hands += self.play(hand_rhs, dealer_upcard)

                case _:
                    hands.append(self._play_hand(hand, dealer_upcard))
            return hands

    def _play_hand(self, hand: Hand, dealer_upcard: Card) -> Hand:
        while not hand.is_bust():
            decision = self.strategy.decide(hand, dealer_upcard)

            match decision:
                case Decision.HIT:
                    hand.add(self.deck.deal())
                case Decision.STAND:
                    break
                case _:
                    raise RuntimeError(
                        f"Can't take decision: {decision} on hand: {hand}"
                    )

        return hand
