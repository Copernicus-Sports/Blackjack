from tests.mocks.mock_deck import MockDeck

from gameplay.dealer import Dealer
from cards.card import Card
from gameplay.rules import Rules
from cards.hand import HandType


def test_dealer_stops_above_seventeen():
    deck = MockDeck()

    deck.load(Card.TEN)
    deck.load(Card.EIGHT)
    deck.load(Card.FIVE)

    dealer = Dealer(deck, [])

    hand = dealer.play()

    assert not deck.empty()
    assert hand.value == 18


def test_dealer_hits_soft_seventeen_based_on_rules():
    deck = MockDeck()

    deck.load(Card.ACE)
    deck.load(Card.SIX)
    deck.load(Card.TEN)

    dealer = Dealer(deck, [Rules.DEALER_HIT_SOFT_SEVENTEEN])

    hand = dealer.play()

    assert deck.empty()
    assert hand.value == 17
    assert hand.type == HandType.HARD


def test_dealer_doesnt_hit_soft_seventeen_based_on_rules():
    deck = MockDeck()

    deck.load(Card.ACE)
    deck.load(Card.SIX)
    deck.load(Card.TEN)

    dealer = Dealer(deck, [])

    hand = dealer.play()

    assert not deck.empty()
    assert hand.value == 17
    assert hand.type == HandType.SOFT
