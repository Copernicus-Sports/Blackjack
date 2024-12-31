from gameplay.player import Player
from gameplay.dealer import Dealer
from cards.hand import Hand, HandEvaluator


class Game:
    @staticmethod
    def play(player: Player, dealer: Dealer) -> float:
        hands = player.play(Hand(), dealer.upcard)

        dealer_hand = dealer.play()

        return sum(
            [HandEvaluator.evaluate(hand, dealer_hand) for hand in hands]
        )
