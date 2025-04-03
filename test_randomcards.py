import pytest
from test import compare_cards

def test_compare_cards_player1_wins():
    assert compare_cards(('K', '♠'), ('J', '♡')) == 1  # King beats Jack
    print("Player 1 wins!")


def test_compare_cards_player2_wins():
    assert compare_cards(('5', '♢'), ('9', '♣')) == -3  # 5 is lower than 9
    print("Player 2 wins!")

def test_compare_cards_tie():
    assert compare_cards(('A', '♠'), ('A', '♡')) == 0  # Both Aces are equal
    print("It's a tie!! Good Game!")