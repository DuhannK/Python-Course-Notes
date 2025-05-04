import pytest
from project import deal_hands, is_playable, choose_card_from_bot

def test_deal_hands():
    hand = deal_hands()
    assert len(hand) == 7


def test_is_playable():
    assert is_playable("🟦0", "🟦1") == True
    assert is_playable("🟥1", "🟦1") == True
    assert is_playable("⬛Wild", "🟦🟥🟨🟩") == True
    assert is_playable("🟥1", "🟦0") == False


def test_choose_card_from_bot():
    assert choose_card_from_bot(["🟦0","🟦1","🟥1"], "🟦2") == ("🟦0", True, "not_black")
    assert choose_card_from_bot(["🟦0","🟦1","🟥1"], "🟩1") == ("🟦1", True, "not_black")
    assert choose_card_from_bot(["🟦0","🟦1","🟥1"], "🟨3") == ("", False, "not_black")
    assert choose_card_from_bot(["🟦0","🟦1","🟥1", "⬛Wild"], "🟨3") == ("⬛Wild", True, "🟦")
