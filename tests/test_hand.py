import pytest

from cards.hand import Hand, HandType
from cards.card import Card


def test_hand_type_bust():
    hand = Hand()

    hand.add(Card.TEN)
    hand.add(Card.EIGHT)
    hand.add(Card.SEVEN)

    assert hand.is_bust()


def test_soft_hand():
    hand = Hand()

    hand.add(Card.SEVEN)
    hand.add(Card.ACE)

    assert hand.type == HandType.SOFT
    assert hand.value == 18

    hand.add(Card.EIGHT)

    assert hand.type == HandType.HARD
    assert hand.value == 16

    hand.add(Card.ACE)

    assert hand.type == HandType.HARD
    assert hand.value == 17


def test_blackjack():
    hand = Hand()

    hand.add(Card.KING)
    hand.add(Card.ACE)

    assert hand.is_blackjack()


def test_pair():
    hand = Hand()

    hand.add(Card.ACE)
    hand.add(Card.ACE)

    assert hand.is_pair()


def test_split():
    hand = Hand()

    hand.add(Card.FIVE)
    hand.add(Card.FIVE)

    hand_lhs, hand_rhs = hand.split()

    assert hand_lhs.value == 5 and hand_rhs.value == 5


def test_split_fails_for_non_pair():
    hand = Hand()

    hand.add(Card.FIVE)
    hand.add(Card.SIX)

    with pytest.raises(AssertionError):
        _, _ = hand.split()
