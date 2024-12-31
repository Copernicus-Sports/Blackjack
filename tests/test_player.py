from tests.mocks.mock_deck import MockDeck

from gameplay.player import Player
from cards.card import Card
from cards.hand import Hand
from sims.strategy import Strategy, Decision


def test_strategy_single_hand():
    strat = Strategy()
    deck = MockDeck()

    deck.load(Card.SEVEN)
    deck.load(Card.THREE)

    upcard = Card.THREE

    strat.hard_hands[(8, Card.THREE)] = Decision.HIT
    strat.hard_hands[(15, Card.THREE)] = Decision.HIT
    strat.hard_hands[(18, Card.THREE)] = Decision.STAND

    player = Player(deck, strat)

    hand = Hand()
    hand.add(Card.FIVE)
    hand.add(Card.THREE)

    result = player.play(hand, upcard)

    assert len(result) == 1 and result[0].value == 18


def test_split_hand():
    strat = Strategy()
    deck = MockDeck()

    hand = Hand()

    hand.add(Card.EIGHT)
    hand.add(Card.EIGHT)

    deck.load(Card.JACK)
    deck.load(Card.THREE)
    deck.load(Card.TEN)

    upcard = Card.THREE

    strat.pairs[(Card.EIGHT, upcard)] = Decision.SPLIT

    strat.hard_hands[(8, upcard)] = Decision.HIT
    strat.hard_hands[(18, upcard)] = Decision.STAND
    strat.hard_hands[(11, upcard)] = Decision.HIT
    strat.hard_hands[(21, upcard)] = Decision.STAND

    player = Player(deck, strat)

    results = player.play(hand, upcard)

    assert (
        len(results) == 2 and results[0].value == 18 and results[1].value == 21
    )


def test_soft_hand():
    strat = Strategy()
    deck = MockDeck()

    hand = Hand()

    hand.add(Card.ACE)
    hand.add(Card.THREE)

    upcard = Card.SEVEN

    deck.load(Card.NINE)
    deck.load(Card.FIVE)

    strat.soft_hands[(14, upcard)] = Decision.HIT
    strat.hard_hands[(13, upcard)] = Decision.HIT
    strat.hard_hands[(18, upcard)] = Decision.STAND

    player = Player(deck, strat)

    results = player.play(hand, upcard)

    assert len(results) == 1 and results[0].value == 18


def test_combo_hand():
    strat = Strategy()
    deck = MockDeck()

    hand = Hand()

    upcard = Card.EIGHT

    hand.add(Card.ACE)
    hand.add(Card.ACE)

    deck.load(Card.JACK)
    deck.load(Card.ACE)
    deck.load(Card.THREE)
    deck.load(Card.QUEEN)
    deck.load(Card.QUEEN)
    deck.load(Card.EIGHT)

    strat.pairs[(Card.ACE, upcard)] = Decision.SPLIT

    strat.soft_hands[(21, upcard)] = Decision.STAND
    strat.soft_hands[(18, upcard)] = Decision.STAND

    strat.soft_hands[(20, upcard)] = Decision.STAND
    strat.hard_hands[(20, upcard)] = Decision.STAND
    strat.soft_hands[(14, upcard)] = Decision.HIT
    strat.hard_hands[(14, upcard)] = Decision.HIT

    player = Player(deck, strat)

    results = player.play(hand, upcard)

    assert len(results) == 3
    assert results[0].is_blackjack()
    assert results[1].is_bust()
    assert results[2].is_blackjack()
