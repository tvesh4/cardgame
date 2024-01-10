import random

suits = ["♠", "♥", "♦", "♣"]
numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#print("Preface \nCoding")

def generate_card_ascii(value, suit):
    top = "---------------\n"

    if value == "10":
        middle = f"|  {value}           |\n"
    else:
        middle = f"|  {value}            |\n"

    middle += "|               |\n"
    middle += f"|      {suit}        |\n"
    middle += "|               |\n"

    if value == "10":
        middle += f"|            {value}   |\n"
    else:
        middle += f"|             {value}  |\n"

    bottom = "---------------\n"

    card = top + middle + bottom
    return card

file_path = "/Users/tveshakumar/Desktop/cards.txt"

with open(file_path, "w") as f:
    for suit in suits:
        for number in numbers:
            card = generate_card_ascii(number, suit)
            f.write(card)
            f.write("-")

def random_cards_generator(number):
    with open(file_path, "r") as f:
        all_cards = f.read().split("-")[:-1]
        cards = random.sample(all_cards, k=number)
        for card in cards:
            print(card)

random_cards_generator(3)