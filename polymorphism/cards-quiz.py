import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8",
         "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    def __eq__(self, other):
        # The "equal to" operator should check that the rank AND suit are equal.
        return self.rank_index == other.rank_index and self.suit_index == other.suit_index

    def __lt__(self, other):
        # A card is "less than" another card if it has a lower rank
        # However, if the ranks are the same, the card with the lower suit is "less than" the other card
        if self.rank_index == other.rank_index:
            return self.suit_index < other.suit_index
        return self.rank_index < other.rank_index

    def __gt__(self, other):
        # A card is "greater than" another card if it has a higher rank.
        # However, if the ranks are the same, the card with the higher suit is "greater than" the other card.
        if self.rank_index == other.rank_index:
            return self.suit_index > other.suit_index
        return self.rank_index > other.rank_index

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"


SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8",
         "9", "10", "Jack", "Queen", "King", "Ace"]

run_cases = [
    ("Ace", "Hearts", "Queen", "Hearts", False, True),
    ("2", "Spades", "2", "Hearts", False, True),
]

submit_cases = run_cases + [
    ("Ace", "Spades", "Ace", "Spades", True, False),
    ("3", "Diamonds", "7", "Clubs", False, False),
    ("King", "Clubs", "King", "Hearts", False, False),
    ("Queen", "Diamonds", "Jack", "Spades", False, True),
    ("10", "Hearts", "10", "Hearts", True, False),
]


def test(rank_1, suit_1, rank_2, suit_2, expected_eq, expected_gt):
    print("---------------------------------")
    print(f"Inputs: {rank_1} of {suit_1}, {rank_2} of {suit_2}")
    print("Expected:")
    print(f" * Equal: {expected_eq}")
    print(f" * Greater than: {expected_gt}")
    print(f" * Less than: {not (expected_eq or expected_gt)}")

    card_1 = Card(rank_1, suit_1)
    card_2 = Card(rank_2, suit_2)
    result_eq = card_1 == card_2
    result_gt = card_1 > card_2
    result_lt = card_1 < card_2
    print("Actual:")
    print(f" * Equal: {result_eq}")
    if result_eq != expected_eq:
        print("Fail")
        return False
    print(f" * Greater than: {result_gt}")
    if result_gt != expected_gt:
        print("Fail")
        return False
    print(f" * Less than: {result_lt}")
    if result_lt == (expected_eq or expected_gt or None):
        print("Fail")
        return False
    print("Pass")
    return True


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
