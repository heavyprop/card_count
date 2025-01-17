import math
import random
import time

# reason we have a card object is if we want to store more information about the card later...
class Card:
    
    def __init__(self, value):
        valid_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        if value not in valid_cards:
            print(f"Invalid card value: {value}. Must be one of {valid_cards}")

        self.value = value

    def __repr__(self):
        return f"{self.value}"

class Deck:
    
    def __init__(self, num_decks):
        self.count = 0
        self.cards = []
        self.num_decks = num_decks
        self.num_card = 0

    def print_deck(self):
        for card in self.cards:
            print(f"Card: {card}")
        print(f"The number of deck left {self.num_decks}")
    
    def add_to_deck(self, card):
        # check how many decks are left for the true count
        self.num_card += 1
        if self.num_card == 52:
            self.num_card = 0
            self.num_decks -= 1
        
        self.cards.append(card)
        self.update_count(card)
    
    def update_count(self, card):
        if card.value in ['2', '3', '4', '5', '6']:
            self.count += 1
        elif card.value in ['10', 'J', 'Q', 'K', 'A']:
            self.count -= 1
        
        # get the true count
        self.get_true_count()
    
    # get the true count, which is the running count / num of decks left
    # then prints out the true count
    def get_true_count(self):
        
        true_count = math.ceil(self.count / self.num_decks)
        self.print_true_count(true_count)
        
    def print_true_count(self, true_count):
        
        if true_count > 3:
            print()
            print(f"!!!! True count is {true_count}, BET BIG !!!!")
            print()
        
        elif true_count == 3:
            print()
            print(f"!!!! True count is {true_count}, INCREASE BET !!!!")
            print()

        elif true_count == 2:
            print()
            print(f"True count is {true_count}, good! !!!!")
            print()
        
        else:
            print()
            print(f"Pick what you want to do? true count is: {true_count}")
            print()


if __name__ == "__main__":
    deck1 = Deck(3)

    # for x in range(103):
    #     deck1.add_to_deck(Card(f"{random.randint(2, 5)}"))
    #     time.sleep(1)

    # deck1.print_deck()

    running = True
    while running == True:
        
        card = str(input("card = "))
        
        if card == "stop":
            running = False

        if card == "help":
            deck1.print_deck()
        
        deck1.add_to_deck(Card(f"{card}"))




