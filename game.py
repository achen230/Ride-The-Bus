import random
import matplotlib.pyplot as plt
from collections import Counter

# Deck is 0–51: 13 cards per suit (Spades, Clubs, Diamonds, Hearts)
def shuffle_deck():
    deck = list(range(0, 52))  # Includes 51
    random.shuffle(deck)
    return deck

def draw_card(deck):
    if deck:
        return deck.pop(0)
    return None

def get_rank(card):
    return (card % 13) + 1  # Normalize to 1–13 (Ace–King)

def get_suit(card):
    if 0 <= card <= 12:
        return "spades"
    elif 13 <= card <= 25:
        return "clubs"
    elif 26 <= card <= 38:
        return "diamonds"
    else:
        return "hearts"

def play_game1():
    while True:
        deck = shuffle_deck()
        counter = 0

        while True:
            drawn_cards = []

            # Step 1: Red or Black
            c1 = draw_card(deck)
            if c1 is None:  # Handle empty deck
                print("Deck is empty. Exiting game.")
                return counter
            drawn_cards.append(c1)
            call = random.choice(["red", "black"])
            if (call == "red" and c1 > 25) or (call == "black" and c1 <= 25):
                pass
            else:
                counter += 1
                continue

            # Step 2: Higher or Lower
            c2 = draw_card(deck)
            if c2 is None:  # Handle empty deck
                print("Deck is empty. Exiting game.")
                return counter
            drawn_cards.append(c2)
            r1 = get_rank(c1)
            r2 = get_rank(c2)

            if random.random() > 0.30:
                if r1 <= 6:
                    if r2 <= r1:
                        pass
                    else:
                        counter += 1
                        continue
                else:
                    if r2 >= r1:
                        pass
                    else:
                        counter += 1
                        continue
            else:
                if random.random() < r2 / 13:
                    if r2 <= r1:
                        pass
                    else:
                        counter += 1
                        continue
                else:
                    if r2 >= r1:
                        pass
                    else:
                        counter += 1
                        continue

            # Step 3: In Between or Outside
            c3 = draw_card(deck)
            if c3 is None:  # Handle empty deck
                print("Deck is empty. Exiting game.")
                return counter
            drawn_cards.append(c3)
            r3 = get_rank(c3)

            low, high = min(r1, r2), max(r1, r2)
            if random.random() > 0.30:
                if abs(r1 - r2) > 6:
                    if r3 <= low or r3 >= high:
                        pass
                    else:
                        counter += 1
                        continue
                else:
                    if low <= r3 <= high:
                        pass
                    else:
                        counter += 1
                        continue
            else:
                if abs(r1 / 13 - r2 / 13) > random.random():
                    if r3 <= low or r3 >= high:
                        pass
                    else:
                        counter += 1
                        continue
                else:
                    if low <= r3 <= high:
                        pass
                    else:
                        counter += 1
                        continue

            # Step 4: Suit guess (must be Spades)
            c4 = draw_card(deck)
            if c4 is None:  # Handle empty deck
                print("Deck is empty. Exiting game.")
                return counter
            drawn_cards.append(c4)
            if get_suit(c4) == "spades":
                print("Success on try:", counter)
                return counter
            else:
                counter += 1
                continue

# Collect results
array_of_games = []
for i in range(1000):
    try:
        result = play_game1()
        array_of_games.append(result)
        if (i + 1) % 100 == 0:
            print(f"{i + 1} games completed")
    except Exception as e:
        print(f"Error in game {i + 1}: {e}")

print(f"Collected {len(array_of_games)} finished games.")

result_distribution = Counter(array_of_games)
x = list(result_distribution.keys())
y = list(result_distribution.values())

plt.bar(x, y, color='blue', alpha=0.7)
plt.xlabel('Number of Attempts')
plt.ylabel('Frequency')
plt.title('Distribution of Attempts to Win')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()